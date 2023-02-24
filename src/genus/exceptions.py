"""
genus.exceptions
----------------
Exceptions that genus can raise during operation.
"""


class UnmatchingSizesException(Exception):
    """Exception for sizes that should match but don't"""

    def __init__(self, size: int, expected: int) -> None:
        super().__init__(f"Expected size {expected}, found {size}")
