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


def main(
    members=100,
    elitism_size=10,
    chrom_size=20,
    one_prob=0.5,
    cross_num=1,
    cross_prob=1,
    mut_prob=0.001,
    generations=200,
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
        members, chrom_size, _fitness, criterion_kwargs={"p": one_prob}
    )
    pipeline = genus.Sequential(
        genus.Parallel(
            genus.ElitismSelection(elitism_size),
            genus.BinaryCrossover(members - elitism_size, cross_num, cross_prob),
        ),
        genus.Join(),
        genus.Mutation(mut_prob),
    )

    for _ in range(generations):
        population = pipeline(population)
        print(population.max_fitness(), population.mean_fitness())

    print(f"Best chromosome: {population.max_member()}")
