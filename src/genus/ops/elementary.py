"""
genus.ops.elementary
---------------------------
Elementary operations between Populations.
"""

from typing import Iterator

from genus.ops.operation import Operation
from genus.types import concatenate, Concatenable


class Identity(Operation):
    """Operation that does nothing"""

    def forward(self, x: object) -> object:
        return x


class Join(Operation):
    """Join multiple populations"""

    def forward(self, x: Iterator[Concatenable]) -> Concatenable:
        return concatenate(*x)
