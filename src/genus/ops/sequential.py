"""
genus.ops.sequential
---------------------------
Meta-operation that contains operations that are applied sequentially.
"""

from typing import Callable, Iterator

from genus.ops.operation import Operation


class Sequential(Operation):
    """Series of operations applied sequentally"""

    def __init__(
        self,
        *operations: Operation,
        _update_function: Callable[[object, Operation], object] = lambda x, op: op(x),
    ) -> None:
        super().__init__()
        self.operations = operations

        # _update_function is useful for debugging
        self._update_function = _update_function

    def __iter__(self) -> Iterator[Operation]:
        return iter(self.operations)

    def forward(self, x: object) -> object:
        for op in self:
            x = self._update_function(x, op)
        return x
