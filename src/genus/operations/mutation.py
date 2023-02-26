"""
genus.operations.mutation
-------------------------
Code for the mutation of chromosomes.
"""

from typing import Iterator

import numpy as np

from genus.chromosome import Chromosome
from genus.operations.operation import Operation


def _flip_bit(code, idx):
    bit = code[idx]
    if bit == "1":
        bit = "0"
    else:
        bit = "1"
    return f"{code[:idx]}{bit}{code[idx + 1:]}"


class BinaryMutation(Operation):
    """Mutation operation, which randomly flips bits"""

    def __init__(self, mutation_probability=0.001) -> None:
        super().__init__()
        self.prob = mutation_probability

    def forward(self, x: Iterator[Chromosome]) -> Iterator[Chromosome]:
        for c in x:
            for i, _ in enumerate(c):
                if np.random.default_rng().random() <= self.prob:
                    c.code = _flip_bit(c.code, i)
        return x
