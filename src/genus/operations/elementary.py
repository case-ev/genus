"""
genus.operations.elementary
---------------------------
Elementary operations between Populations.
"""

from typing import Iterator

from genus_utils.logger import LOGGER

from genus.operations.operation import Operation
from genus.population import Population, join


class Identity(Operation):
    """Operation that does nothing"""

    def forward(self, x: object) -> object:
        LOGGER.debug("Applying Identity operation")
        return x


class Join(Operation):
    """Join multiple populations"""

    def forward(self, x: Iterator[Population]) -> Population:
        return join(*x)
