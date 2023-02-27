"""
genus
=====
*genus* is a library that allows the creation and simulation of evolution,
using genetic algorithms.
"""

from . import ops
from .chromosome import Chromosome
from .population import Population
from .types import Concatenable, concatenate


__all__ = [
    "ops",
    "Chromosome",
    "Population",
    "Concatenable",
    "concatenate",
]
