"""
genus.ops.parallel
---------------------------
Meta-operation that contains operations that are applied in parallel.
"""

from typing import Callable, List
import concurrent.futures

from genus.ops.operation import Operation


class Parallel(Operation):
    """Apply multiple operations on parallel"""

    def __init__(
        self,
        *operations: Operation,
        _update_function: Callable[[object, Operation], object] = lambda x, op: op(x),
    ) -> None:
        super().__init__()
        self.operations = operations
        self._update_function = _update_function

    def forward(self, x: object) -> List:
        # Use multithreading to speed up the execution
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self._update_function, x, op) for op in self.operations
            ]
            return [f.result() for f in futures]
