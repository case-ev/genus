"""
genus.operations.mutation
-------------------------
Code for the mutation of chromosomes.
"""

from typing import List

import numpy as np

from genus.chromosome import Chromosome
from genus.operations.operation import Operation


def _flip_bit(bit):
    if bit == "0":
        return "1"
    return "0"


class Mutation(Operation):
    """Mutation operation, which randomly flips bits"""

    def __init__(self, mutation_probability=0.001) -> None:
        super().__init__()
        self.prob = mutation_probability

    def forward(self, x: List[Chromosome]) -> List[Chromosome]:
        for c in x:
            for i, bit in enumerate(c):
                if np.random.default_rng().random() <= self.prob:
                    c[i] = _flip_bit(bit)
        return x
