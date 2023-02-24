"""Unit tests for elitism selection."""

from genus import Chromosome, ElitismSelection


def _basic_fitness(chromosome):
    return chromosome.code.count("1")


def test_basic():
    """Test elitism with a basic fitness function"""
    chromosomes = [Chromosome(code="1" * i + "0" * (10 - i)) for i in range(11)]
    sel = ElitismSelection(_basic_fitness, 5)
    chosen = sel(chromosomes)
    assert len(chosen) == 5
    for c in chosen:
        assert c.code.count("1") >= 6

    sel = ElitismSelection(_basic_fitness, proportion=0.5)
    chosen = sel(chromosomes)
    assert len(chosen) == 5
    for c in chosen:
        assert c.code.count("1") >= 6
