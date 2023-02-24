"""
genus.operations.sequential
---------------------------
Sequential application of operations on chromosomes.
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
