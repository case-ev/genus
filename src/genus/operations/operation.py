"""
genus.operations.operation
----------------
Base interface for operations applied on chromosomes.
"""

import abc


class Operation(abc.ABC):
    """Interface for operations performed on chromosomes"""

    @abc.abstractmethod
    def forward(self, x: object) -> object:
        """Do a forward pass of the operation"""

    def __call__(self, x: object) -> object:
        return self.forward(x)
