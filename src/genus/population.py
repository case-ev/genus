"""
genus.population
----------------
Code for handling a population of chromosomes.
"""

from typing import Callable, Dict, Iterator, List, Self

import numpy as np

from genus.chromosome import Chromosome
from genus.types import Concatenable


class Population(Concatenable):
    """Population of chromosomes"""

    def __init__(
        self,
        members: List[Chromosome],
        fitness: Callable[[Chromosome], float],
    ) -> None:
        self.members = members
        self.fitness = fitness

    @classmethod
    def from_num(
        cls,
        member_total: int,
        chrom_size: int,
        fitness: Callable[[Chromosome], float],
        *,
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
            fitness,
            **kwargs,
        )

    def __eq__(self, o: object) -> bool:
        try:
            return o.members == self.members and o.fitness == self.fitness
        except AttributeError:
            return False

    def __getitem__(self, key: object) -> Chromosome:
        return self.members[key]

    def __setitem__(self, key: object, new_ch: Chromosome) -> None:
        self.members[key] = new_ch

    def __iter__(self) -> Iterator[Chromosome]:
        return iter(self.members)

    def __len__(self) -> int:
        return len(self.members)

    def member_fitness(self) -> List[float]:
        """Get the fitness of all members"""
        return [self.fitness(c) for c in self.members]

    def max_fitness(self) -> float:
        """Get the max fitness"""
        return np.max(self.member_fitness())

    def max_member(self) -> Chromosome:
        """Get the chromosome with the max fitness"""
        return self.members[np.argmax(self.member_fitness())]

    def min_fitness(self) -> float:
        """Get the min fitness"""
        return np.min(self.member_fitness())

    def min_member(self) -> Chromosome:
        """Get the chromosome with the min fitness"""
        return self.members[np.argmin(self.member_fitness())]

    def mean_fitness(self) -> float:
        """Get the average fitness"""
        return np.mean(self.member_fitness())

    def std_fitness(self) -> float:
        """Get the standard deviation of fitness"""
        return np.std(self.member_fitness())

    def concatenate(self, *populations, fitness: Callable[[Chromosome], float] = None, **_) -> Self:
        """Concatenate this population to a series of other populations. If
        no fitness function is given, it takes the one from this population.

        Parameters
        ----------
        *populations: Population
            Populations to concatenate.
        fitness: Callable[[Chromosome], float], optional
            Fitness function to use, by default None. If None, it uses the
            fitness function of this population.

        Returns
        -------
        Population
            Joint population.
        """
        members = self.members.copy()
        for p in populations:
            members.extend(p.members)
        return Population(members, self.fitness if fitness is None else fitness)
