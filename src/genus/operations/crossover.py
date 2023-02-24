"""
genus.operations.crossover
--------------------------
Code for the crossover operation, which takes two chromosomes, splits
them and joins them.
"""

from typing import Callable, List, Tuple

import numpy as np

from genus_utils.logger import LOGGER

from genus.exceptions import UnmatchingSizesException
from genus.chromosome import Chromosome, concatenate
from genus.population import Population
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


def _probfn_normalize(pop):
    fitness_vals = pop.member_fitness()
    total_fitness = np.sum(fitness_vals)
    return [f / total_fitness for f in fitness_vals]


class BinaryCrossover(Operation):
    """Binary crossover operation, whick uses two parents"""

    def __init__(self, size=None, cross_num=1, cross_probability=1, probability_function: Callable[[Population], float] = _probfn_normalize) -> None:
        super().__init__()
        self.size = size
        self.cross_num = cross_num
        self.cross_probability = cross_probability
        self._prob_fn = probability_function

    def forward(self, x: Population) -> Population:
        LOGGER.debug(
            "Applying crossover operation with probability %.2f%%",
            100 * self.cross_probability,
        )
        rng = np.random.default_rng()
        probabilities = self._prob_fn(x)

        # If self mating occurs it would mean that the parent has an amazing fitness
        parents = rng.choice(x, self.size, p=probabilities)
        children = []
        p1 = parents[::2]
        p2 = parents[1::2]
        for a, b in zip(p1, p2):
            if rng.random() <= self.cross_probability:
                children.extend(cross_pair(a, b, self.cross_num))
            else:
                children.extend((a, b))

        if (l := len(children)) != self.size:
            LOGGER.error("Size of children and origin do not match")
            raise UnmatchingSizesException(l, self.size)
        return Population(children, x.fitness)
