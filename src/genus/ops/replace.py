"""
genus.ops.replace
-----------------
Operations for replacing members of a population for new members, in order to
introduce artificial variance to the genetic code.
"""

from typing import List

from genus.chromosome import Chromosome
from genus.exceptions import UnmatchingSizesException
from genus.population import Population
from genus.ops.operation import Operation


class ReplaceNWorst(Operation):
    """Replaces some number of the worst members by random chromosomes"""

    def __init__(
        self, amount: int, chroms: Chromosome | List[Chromosome] = None, **chrom_kwargs
    ) -> None:
        super().__init__()
        self.amount = amount
        self.chroms = chroms
        self.chrom_kwargs = chrom_kwargs
        if chroms is not None:
            try:
                if len(chroms) != amount:
                    raise UnmatchingSizesException(len(chroms), amount)
            except ValueError:
                # Raised if a single chromosome is given
                self.chroms = [chroms for _ in range(amount)]

    def forward(self, x: Population) -> Population:
        new_chroms = (
            self.chroms
            if self.chroms is not None
            else [Chromosome.from_size(x[0].size, **self.chrom_kwargs)]
        )
        fitness = x.member_fitness()
        x[fitness.argsort()[: self.amount]] = new_chroms
        return x
