"""
genus.operations.meta_operations
---------------------------
Operations that use other operations as a base.
"""

from typing import Callable, Iterator, List
import concurrent.futures

from genus.operations.operation import Operation


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


class Parallel(Operation):
    """Apply multiple operations on parallel"""

    def __init__(self, *operations: Operation) -> None:
        super().__init__()
        self.operations = operations

    def forward(self, x: object) -> List:
        # Use multithreading to speed up the execution
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(op, x) for op in self.operations]
            return [f.result() for f in futures]
