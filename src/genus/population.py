"""
genus.population
----------------
Code for handling a population of chromosomes.
"""

from typing import Callable, Dict, Iterator, List, Self

import numpy as np

from genus.chromosome import Chromosome


class Population:
    """Population of chromosomes"""

    def __init__(
        self,
        members: List[Chromosome],
        fitness: Callable[[Chromosome], float],
    ) -> None:
        self.members = members
        self.fitness_function = fitness

    @classmethod
    def from_num(
        cls,
        member_total: int,
        chrom_size: int,
        criterion: str = "random_binary",
        criterion_kwargs: Dict = None,
        **kwargs
    ) -> Self:
        """Create a population from a total amount of members and the
        size of each chromosome.

        Parameters
        ----------
        member_total : int
            Total amount of chromosomes in the population.
        chrom_size : int
            Size of each chromosome.
        criterion : str, optional
            Criterion to use for the generation of chromosomes, by
            default "random_binary".

        Returns
        -------
        Population
            Population of chromosomes.
        """
        criterion_kwargs = {} if criterion_kwargs is None else criterion_kwargs
        return cls(
            [
                Chromosome.from_size(chrom_size, criterion, **criterion_kwargs)
                for _ in range(member_total)
            ],
            **kwargs,
        )

    def __getitem__(self, key: object) -> Chromosome:
        return self.members[key]

    def __setitem__(self, key: object, new_ch: Chromosome) -> None:
        self.members[key] = new_ch

    def __iter__(self) -> Iterator[Chromosome]:
        return iter(self.members)

    def member_fitness(self) -> List[float]:
        """Get the fitness of all members"""
        return [self.fitness_function(c) for c in self.members]

    def max_fitness(self) -> float:
        """Get the max fitness"""
        return np.max(self.member_fitness())

    def min_fitness(self) -> float:
        """Get the min fitness"""
        return np.min(self.member_fitness())

    def mean_fitness(self) -> float:
        """Get the average fitness"""
        return np.mean(self.member_fitness())

    def std_fitness(self) -> float:
        """Get the standard deviation of fitness"""
        return np.std(self.member_fitness())
