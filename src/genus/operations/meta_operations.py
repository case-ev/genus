"""
genus.operations.meta_operations
---------------------------
Operations that use other operations as a base.
"""

from typing import Iterator

from genus.operations.operation import Operation


class Sequential(Operation):
    """Series of operations applied sequentally"""

    def __init__(self, *operations: Operation) -> None:
        self.operations = operations

    def __iter__(self) -> Iterator[Operation]:
        return iter(self.operations)

    def forward(self, x: object) -> object:
        for op in self:
            x = op(x)
        return x


class Identity(Operation):
    """Operation that does nothing"""

    def forward(self, x: object) -> object:
        return x
