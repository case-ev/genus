"""
genus.operations
----------------
Module for the operations that can be applied on a chromosome or population
of chromosomes.

All operations are based on the `Operation` interface, which is based on the
way PyTorch handles operations. In this sense, `Operation` would be similar
to `torch.nn.Module`, even using similar conventions for some names.
"""

from .crossover import TwoParentCrossover, cross_pair
from .elementary import Identity, Join
from .meta_operations import Sequential, Parallel
from .mutation import BinaryMutation
from .operation import Operation
from .selection import ElitismSelection


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
