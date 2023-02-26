"""
genus.operations.operation
----------------
Base interface for operations applied on chromosomes.
"""

import abc

from genus_utils.logger import LOGGER


class Operation(abc.ABC):
    """Interface for operations performed on chromosomes"""

    @abc.abstractmethod
    def forward(self, x: object) -> object:
        """Do a forward pass of the operation"""

    def __call__(self, x: object) -> object:
        LOGGER.debug("Calling %s layer", type(self).__name__)
        return self.forward(x)
