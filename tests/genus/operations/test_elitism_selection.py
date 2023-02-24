"""Unit tests for elitism selection."""

import genus


def _basic_fitness(chromosome):
    return chromosome.code.count("1")


def test_basic():
    """Test elitism with a basic fitness function"""
    chromosomes = [genus.Chromosome("1" * i + "0" * (10 - i)) for i in range(11)]
    sel = genus.ElitismSelection(5)
    chosen = sel(genus.Population(chromosomes, _basic_fitness))
    assert len(chosen) == 5
    for c in chosen:
        assert c.code.count("1") >= 6

    sel = genus.ElitismSelection(proportion=0.5)
    chosen = sel(genus.Population(chromosomes, _basic_fitness))
    assert len(chosen) == 5
    for c in chosen:
        assert c.code.count("1") >= 6
