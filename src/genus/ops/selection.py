"""
genus.ops.selection
--------------------------
Code for the selection operator, which takes a population of chromosomes
and determines which ones are chosen to reproduce.
"""

from genus_utils.logger import LOGGER

from genus.population import Population
from genus.ops.operation import Operation


class ElitismSelection(Operation):
    """Elitism selection operator, which chooses the fittest chromosomes to survive
    to the next generation."""

    def __init__(
        self,
        amount: int = None,
        proportion: float = None,
    ) -> None:
        """Create a configuration for selection using elitism.

        Parameters
        ----------
        amount : int, optional
            Amount of chromosomes to choose as the best, by default None. If
            specified, it takes precedence over whatever value is indicated
            by `proportion`.
        proportion : float, optional
            Proportion of the total size of chromosomes to choose as best,
            by default None. If both `amount` and `proportion` are None,
            it takes all the values.
        """
        super().__init__()
        self.amount = amount
        self.proportion = proportion

    def forward(self, x: Population) -> Population:
        values = sorted(x.members, key=x.fitness, reverse=True)
        if self.amount is not None:
            return Population(values[: self.amount], x.fitness)
        if self.proportion is not None:
            size = int(len(values) * self.proportion)
            return Population(values[:size], x.fitness)
        LOGGER.warning(
            "Neither amount or proportion were specified, returning all values"
        )
        return Population(values, x.fitness)
