"""Unit tests for the crossover operation"""

import genus


def test_1():
    """Test 1 for crossover"""
    c1 = genus.Chromosome(code="000000000000")
    c2 = genus.Chromosome(code="111111111111")

    cross1, cross2 = genus.cross_pair(c1, c2, None, _cross_points=(4, 8, 10))
    assert str(cross1) == "000011110011"
    assert str(cross2) == "111100001100"

    cross1, cross2 = genus.cross_pair(c1, c2)
    for a, b in zip(cross1, cross2):
        assert a != b

    empty1 = genus.Chromosome(0)
    empty2 = genus.Chromosome(0)
    cross1, cross2 = genus.cross_pair(empty1, empty2)
    assert str(cross1) == ""
    assert str(cross2) == ""
    assert empty1 == empty2 == cross1 == cross2
