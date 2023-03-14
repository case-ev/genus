"""
genus.ops
----------------
Module for the operations that can be applied on a chromosome or population
of chromosomes.

All operations are based on the `Operation` interface, which is based on the
way PyTorch handles operations. In this sense, `Operation` would be similar
to `torch.nn.Module`, even using similar conventions for some names.
"""

from .crossover import TwoParentCrossover, cross_pair
from .elementary import Identity, Join
from .mutation import BinaryMutation
from .operation import Operation
from .parallel import Parallel
from .selection import ElitismSelection
from .sequential import Sequential


__all__ = [
    "TwoParentCrossover",
    "cross_pair",
    "Identity",
    "Join",
    "Sequential",
    "Parallel",
    "BinaryMutation",
    "Operation",
    "ElitismSelection",
]
