"""Unit tests for elitism selection."""

import genus


def _basic_fitness(chromosome):
    return (chromosome.code == 1).sum()


def test_basic():
    """Test elitism with a basic fitness function"""
    chromosomes = [genus.Chromosome.from_str("1" * i + "0" * (10 - i)) for i in range(11)]
    sel = genus.ops.ElitismSelection(5)
    chosen = sel(genus.Population(chromosomes, _basic_fitness))
    assert len(chosen) == 5
    for c in chosen:
        assert (c.code == 1).sum() >= 6

    sel = genus.ops.ElitismSelection(proportion=0.5)
    chosen = sel(genus.Population(chromosomes, _basic_fitness))
    assert len(chosen) == 5
    for c in chosen:
        assert (c.code == 1).sum() >= 6
