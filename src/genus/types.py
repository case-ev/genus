"""
genus.basic_operations
----------------------
Aliases for some basic operations.
"""

import abc
from typing import Self


class Concatenable(abc.ABC):
    """Interface for items that can be concatenated"""

    @abc.abstractmethod
    def concatenate(self, *items: Self, **kwargs) -> Self:
        """Concatenate items to self"""


def concatenate(*items: Concatenable, **kwargs) -> Concatenable:
    """Concatenate some items"""
    return items[0].concatenate(*items[1:], **kwargs)
