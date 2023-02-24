"""
genus.chromosome
----------------
Code for the creation of chromosomes, which act as the basic data structure.
"""

from typing import Self

import numpy as np

from genus_utils.logger import LOGGER


class Chromosome:
    """Chromosome containing some genetic code for an organism"""

    RNG = np.random.default_rng()

    def __init__(
        self, size: int = None, code: str = None, criterion: str = "random_binary", **kwargs
    ) -> None:
        self._criterion = criterion
        self._criterion_func = globals()[f"__chromosome_init_{criterion}"]
        self._size = size
        self.code = self._criterion_func(size, **kwargs) if code is None else code
        if (real_size := len(self.code)) != size:
            if size is not None:
                LOGGER.warning(
                    "Specified code doesn't match the given size. Changing \
    size to %s",
                    real_size,
                )
            self._size = real_size

    def __setitem__(self, key: object, bit: str) -> None:
        self.code[key] = bit

    def __getitem__(self, key: object) -> str:
        return self.code[key]

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.code == obj.code
        return False

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return f"Chromosome(size={repr(self.size)}, code={repr(self.code)}, \
criterion={repr(self.criterion)})"

    def __str__(self) -> str:
        return self.code

    @property
    def criterion(self) -> str:
        """Criterion used for the initialization of the chromosome"""
        return self._criterion

    @criterion.setter
    def criterion(self, new_criterion: str) -> None:
        self._criterion = new_criterion
        self._criterion_func = globals()[f"__chromosome_init_{new_criterion}"]

    @property
    def size(self) -> int:
        """Size of the chromosome"""
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        LOGGER.warning(
            "Size was changed but to generate new codes run `Chromosome.new_code`"
        )
        self._size = new_size

    def new_code(self) -> str:
        """Generate a new code"""
        self.code = self._criterion_func(self.size)
        return self.code

    def concatenate(self, *chromosomes, **kwargs) -> Self:
        """Concatenate multiple chromosomes end-to-end to this one.

        The concatenation is done following the order in which chromosomes
        are given to the function.

        Parameters
        ----------
        *chromosomes: Chromosome
            Chromosomes to join.
        reverse: bool, optional
            Whether to concatenate in reverse, by default False.

        Returns
        -------
        Chromosome
            Concatenated chromosome.
        """
        return concatenate(self, *chromosomes, **kwargs)


def __chromosome_init_zero(size, **_):
    return "0" * size


def __chromosome_init_random_binary(size, p=0.5, **_):
    return "".join((Chromosome.RNG.random(size) <= p).astype(int).astype(str))


def concatenate(*chromosomes, reverse=False) -> Chromosome:
    """Concatenate multiple chromosomes end-to-end.

    The concatenation is done following the order in which chromosomes
    are given to the function.

    Parameters
    ----------
    *chromosomes: Chromosome
        Chromosomes to join.
    reverse: bool, optional
        Whether to concatenate in reverse, by default False.

    Returns
    -------
    Chromosome
        Concatenated chromosome.
    """
    code = ""
    for c in chromosomes:
        code = f"{c.code}{code}" if reverse else f"{code}{c.code}"
    return Chromosome(code=code, criterion=chromosomes[0].criterion)
