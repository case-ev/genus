"""
genus.operations.mutation
-------------------------
Code for the mutation of chromosomes.
"""

from typing import Iterator

import numpy as np

from genus.chromosome import Chromosome
from genus.operations.operation import Operation


class BinaryMutation(Operation):
    """Mutation operation, which randomly flips bits"""

    def __init__(self, mutation_probability=0.001) -> None:
        super().__init__()
        self.prob = mutation_probability

    def forward(self, x: Iterator[Chromosome]) -> Iterator[Chromosome]:
        for c in x:
            c.flip_bits(np.random.default_rng().random(len(c)) <= self.prob)
        return x
