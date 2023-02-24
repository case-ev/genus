"""
genus.operations.crossover
--------------------------
Code for the crossover operation, which takes two chromosomes, splits
them and joins them.
"""

from typing import List, Tuple

import numpy as np

from genus_utils.logger import LOGGER

from genus.chromosome import Chromosome, concatenate
from genus.operations.operation import Operation


def cross_pair(
    a: Chromosome, b: Chromosome, cross_num: int = 1, *, _cross_points: List[int] = None
) -> Tuple[Chromosome, Chromosome]:
    """Apply crossover to a pair of chromosomes.

    Parameters
    ----------
    a : Chromosome
        First parent chromosome.
    b : Chromosome
        Second parent chromosome.
    cross_num : int, optional
        Number of crosses to apply, by default 1.
    _cross_points: List[int], optional
        Argument to explicitly indicate where to cut the chromosomes, by
        default None. You probably shouldn't use this parameter, as it is
        mainly meant for debugging.

    Returns
    -------
    Tuple[Chromosome, Chromosome]
        Crossed over children.
    """
    if _cross_points is None:
        if (l := len(a)) != 0:
            cross_points = np.random.default_rng().choice(range(l), cross_num, False)
        else:
            LOGGER.warning("Found empty chromosomes")
            cross_points = [0]
    else:
        cross_points = _cross_points
    a_components = a.split(cross_points)
    b_components = b.split(cross_points)
    for i, _ in enumerate(a_components):
        # Swap them if the index is odd
        if i % 2 == 1:
            a_components[i], b_components[i] = b_components[i], a_components[i]
    return concatenate(*a_components), concatenate(*b_components)


class Crossover(Operation):
    """Crossover operation"""

    def __init__(self, size=None, cross_num=1, cross_probability=1) -> None:
        super().__init__()
        self.size = size
        self.cross_num = cross_num
        self.cross_probability = cross_probability

    def forward(self, x: List[Chromosome]) -> List[Chromosome]:
        rng = np.random.default_rng()

        size = self.size
        remaining = None
        if size is None:
            if (l := len(x)) % 2 == 1:
                # We remove the odd element
                remaining = x.pop()
            size = l // 2

        # Choose the first `size` elements
        rng.shuffle(x)
        group1 = x[:size + 2:2]
        group2 = x[1:size + 3:2]
        result = x[2 * size:]       # Puts the remaining ones in `result`

        # Apply the crossover
        for a, b in zip(group1, group2):
            if rng.random() <= self.cross_probability:
                result.extend(cross_pair(a, b, self.cross_num))
            else:
                result.extend((a, b))
        if remaining is not None:
            result.append(remaining)
        return result
