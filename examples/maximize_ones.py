"""
exmples.maximize_ones
---------------------
Example to show a program that maximizes the number of ones in a string
using genetic algorithms.
"""

from genus_utils.logger import LOGGER
import genus


# Counts the number of ones
def _fitness(c: genus.Chromosome) -> float:
    return c.code.count("1")


def main():
    """Maximize the number of ones in a string"""
    pass
