"""
genus.operations.selection
--------------------------
Code for the selection operator, which takes a population of chromosomes
and determines which ones are chosen to reproduce.
"""

from typing import Callable, List

from genus_utils.logger import LOGGER

from genus.chromosome import Chromosome
from genus.operations.operation import Operation


class ElitismSelection(Operation):
    """Elitism selection operator, which chooses the fittest chromosomes to survive
    to the next generation."""

    def __init__(
        self,
        fitness: Callable[[Chromosome], float],
        amount: int = None,
        proportion: float = None,
    ) -> None:
        super().__init__()
        self.fitness = fitness
        self.amount = amount
        self.proportion = proportion

    def forward(self, x: List[Chromosome]) -> List[Chromosome]:
        values = sorted(x, key=self.fitness, reverse=True)
        if self.amount is not None:
            return values[:self.amount]
        if self.proportion is not None:
            size = int(len(values) * self.proportion)
            return values[:size]
        LOGGER.warning("Neither amount or proportion were specified, returning all values")
        return values
