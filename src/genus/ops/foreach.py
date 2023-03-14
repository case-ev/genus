"""
genus.ops.foreach
----------------
Meta-operation that contains an operation that is passed for each element
in the input.
"""

from typing import Iterable

from genus.ops.operation import Operation


class ForEach(Operation):
    """Operation that is applied for each element in the input."""

    def __init__(self, op: Operation) -> None:
        super().__init__()
        self.op = op

    def forward(self, x: Iterable) -> Iterable:
        return [self.op(i) for i in x]
