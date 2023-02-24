"""
genus.operations
----------------
Module for the operations that can be applied on a chromosome or population
of chromosomes.

All operations are based on the `Operation` interface, which is based on the
way PyTorch handles operations. In this sense, `Operation` would be similar
to `torch.nn.Module`, even using similar conventions for some names.
"""

from .crossover import *
from .elementary import *
from .meta_operations import *
from .operation import Operation
from .selection import *
