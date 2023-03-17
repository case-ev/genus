"""
genus.ops.parallel
---------------------------
Meta-operation that contains operations that are applied in parallel.
"""

from typing import Callable, List
import concurrent.futures

from genus.ops.operation import Operation


class Parallel(Operation):
    """Apply multiple operations in parallel, without guaranteeing that
    the results are in the same order as the inputs"""

    def __init__(
        self,
        *operations: Operation,
        _update_function: Callable[[object, Operation], object] = lambda x, op: op(x),
        workers: int = None,
    ) -> None:
        super().__init__()
        self.operations = operations
        self._update_function = _update_function
        self.workers = workers

    def forward(self, x: object) -> List:
        with concurrent.futures.ThreadPoolExecutor(self.workers) as executor:
            return executor.map(lambda arg: self._update_function(*arg), ((x, op) for op in self.operations))


class ParallelOrdered(Operation):
    """Apply multiple operations on parallel, guaranteeing that the order
    of operations is preserved"""

    def __init__(
        self,
        *operations: Operation,
        _update_function: Callable[[object, Operation], object] = lambda x, op: op(x),
        workers: int = None,
    ) -> None:
        super().__init__()
        self.operations = operations
        self._update_function = _update_function
        self.workers = workers

    def forward(self, x: object) -> List:
        with concurrent.futures.ThreadPoolExecutor(self.workers) as executor:
            futures = [
                executor.submit(self._update_function, x, op) for op in self.operations
            ]
            return [f.result() for f in futures]
