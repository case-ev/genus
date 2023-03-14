"""
genus.ops.op_lambda
------------------
Operation that represents a lambda function.
"""

from typing import Callable

from genus.ops.operation import Operation


class Lambda(Operation):
    """Operation for an arbitrary function that is applied to the data."""

    def __init__(self, fn: Callable[[object], object] = None) -> None:
        super().__init__()
        self.fn = fn if fn is not None else lambda x: x

    def forward(self, x: object) -> object:
        return self.fn(x)
