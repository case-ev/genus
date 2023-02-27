"""
genus.chromosome
----------------
Code for the creation of chromosomes, which act as the basic data structure.
"""

from typing import List, Self, Iterator

import numpy as np

from genus.types import Concatenable


def __chromosome_init_zero(size, **_):
    return np.zeros(size, dtype=np.uint8)


def __chromosome_init_random_binary(size, p=0.5, **_):
    return (np.random.default_rng().random(size) <= p).astype(np.uint8)


class Chromosome(Concatenable):
    """Chromosome containing some genetic code for an organism"""

    def __init__(self, code: np.ndarray) -> None:
        self.code = code
        self._size = len(code)

    @property
    def code_str(self):
        """Code as string"""
        return "".join(map(str, self.code))

    @classmethod
    def from_size(cls, size: int, criterion: str = "random_binary", **kwargs) -> Self:
        """Create a chromosome from a size and a criterion"""
        return cls(globals()[f"__chromosome_init_{criterion}"](size, **kwargs))

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.code == obj.code
        return False

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return f"Chromosome(code={repr(self.code)})"

    def __str__(self) -> str:
        return self.code_str

    def __iter__(self) -> Iterator[str]:
        return iter(self.code)

    @property
    def size(self) -> int:
        """Size of the chromosome"""
        return self._size

    def concatenate(self, *chromosomes: Self, reverse=False, **_) -> Self:
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
        _chroms = [*chromosomes[::-1], self] if reverse else [self, *chromosomes]
        code = np.concatenate([c.code for c in _chroms])
        return Chromosome(code)

    def split(self, idx: List[int]) -> List[Self]:
        """Split this chromosome in the indicated indices.

        The indices can either be a single index, indicating one split,
        or a list of indices, indicating multiple cuts.

        Parameters
        ----------
        idx : int or List[int]
            Indices on which to make the cut to the chromosome. If a single
            index is given, the cut is made on that index.

        Returns
        -------
        List[Chromosome]
            Cut up chromosome.
        """
        try:
            result = [Chromosome(code=self.code[: idx[0]])]
            result.extend(
                [Chromosome(code=self.code[p : idx[i + 1]]) for i, p in enumerate(idx[:-1])]
            )
            result.append(Chromosome(code=self.code[idx[-1] :]))
        except TypeError:
            # Raised when there is a single place
            result = [Chromosome(code=self.code[:idx]), Chromosome(code=self.code[idx:])]
        return result

    def flip_bit(self, idx):
        """Flip the bit at a given position"""
        self.code[idx] = not self.code[idx]
        return self.code

    def flip_bits(self, indicators):
        """Flip the bits where `indicators` is 1"""
        self.code = (self.code + indicators) % 2
        return self.code
