"""
genus.operations.meta_operations
---------------------------
Operations that use other operations as a base.
"""

from typing import Callable, Iterator

from genus_utils.logger import LOGGER

from genus.operations.operation import Operation


class Sequential(Operation):
    """Series of operations applied sequentally"""

    def __init__(
        self,
        *operations: Operation,
        _update_function: Callable[[object, Operation], None] = None
    ) -> None:
        super().__init__()
        self.operations = operations

        # _update_function is useful for debugging
        self._update_function = _update_function

    def __iter__(self) -> Iterator[Operation]:
        return iter(self.operations)

    def forward(self, x: object) -> object:
        LOGGER.debug("Applying Sequential operations")
        for op in self:
            if self._update_function is not None:
                self._update_function(x, op)
            x = op(x)
        if self._update_function is not None:
            self._update_function(x, None)
        return x


class Identity(Operation):
    """Operation that does nothing"""

    def forward(self, x: object) -> object:
        LOGGER.debug("Applying Identity operation")
        return x
