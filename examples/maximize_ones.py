"""
exmples.maximize_ones
---------------------
Example to show a program that maximizes the number of ones in a string
using genetic algorithms.
"""

from tqdm import tqdm
from timeit import default_timer as timer

from genus_utils.logger import LOGGER
import genus


# Counts the number of ones
def _fitness(c: genus.Chromosome) -> float:
    return (c.code == 1).sum()


class _Diagnostic:
    def __init__(self) -> None:
        self.dict = {}

    def _get_times(self, _type):
        if (t := self.dict.get(_type)) is not None:
            return t
        return []

    def _append(self, val, _type):
        if (d := self.dict.get(_type)) is not None:
            d.append(val)
        else:
            self.dict[_type] = [val]

    def add_time(self, x, op):
        """Add the time of the operation"""
        start = timer()
        val = op(x)
        end = timer()
        delta = end - start
        self._append(delta, type(op).__name__)
        return val


def main(
    members=100,
    elitism_size=10,
    chrom_size=20,
    one_prob=0.5,
    cross_num=1,
    cross_prob=1,
    mut_prob=0.001,
    generations=200,
    criterion="random_binary",
    diagnostic=False,
):
    """Maximize the number of ones in a string"""
    LOGGER.info("Parsing input arguments")
    members = int(members)
    elitism_size = int(elitism_size)
    chrom_size = int(chrom_size)
    one_prob = float(one_prob)
    cross_num = int(cross_num)
    cross_prob = float(cross_prob)
    mut_prob = float(mut_prob)
    generations = int(generations)

    LOGGER.info("Creating population")
    population = genus.Population.from_num(
        members,
        chrom_size,
        _fitness,
        criterion=criterion,
        criterion_kwargs={"p": one_prob},
    )
    _diagnostic = _Diagnostic()
    pipeline = genus.Sequential(
        genus.Parallel(
            genus.ElitismSelection(elitism_size),
            genus.TwoParentCrossover(members - elitism_size, cross_num, cross_prob),
            _update_function=_diagnostic.add_time,
        ),
        genus.Join(),
        genus.BinaryMutation(mut_prob),
        _update_function=_diagnostic.add_time,
    )

    for _ in (prog_bar := tqdm(range(generations), desc="Optimizing")):
        try:
            population = pipeline(population)
            prog_bar.desc = f"Optimizing, current best is {population.max_member()}"
        except:
            LOGGER.error("Found error, safely ending training")
            break

    print(f"Best chromosome: {population.max_member()}")

    if diagnostic:
        print("\nDiagnostic")
        print("==========")
        for op, times in _diagnostic.dict.items():
            print(f"+ {op:20} -> {1000 * sum(times):12.4f}ms")
