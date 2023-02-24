"""Unit tests for Chromosome"""

from genus import Chromosome, concatenate


def test_creation():
    """Test the creation of chromosomes"""
    c1 = Chromosome(code="01010101")
    c2 = Chromosome(code="01010101")
    assert c1 == c2
    assert len(c1) == 8
    assert len(c2) == 8
    assert c1.size == 8
    assert c2.size == 8

    c1 = Chromosome(10, criterion="zero")
    c2 = Chromosome(10, criterion="zero")
    assert c1 == c2
    assert c1.code == "0000000000"
    assert c2.code == "0000000000"
    assert len(c1) == 10
    assert len(c2) == 10
    assert c1.size == 10
    assert c2.size == 10

    c1 = Chromosome(10, criterion="random")
    c2 = Chromosome(10, criterion="random")
    c1_copy = Chromosome(code=c1.code)
    c2_copy = Chromosome(code=c2.code)
    assert c1 == c1_copy
    assert c2 == c2_copy
    assert len(c1) == 10
    assert len(c2) == 10
    assert c1.size == 10
    assert c2.size == 10

    empty_c1 = Chromosome(0, criterion="random")
    empty_c2 = Chromosome(0, criterion="random")
    assert empty_c1.code == ""
    assert empty_c2.code == ""
    assert empty_c1 == empty_c2
    assert len(empty_c1) == 0
    assert len(empty_c2) == 0
    assert empty_c1.size == 0
    assert empty_c2.size == 0


def test_str():
    """Test strings and repr of chromosomes"""
    c1 = Chromosome(code="01010101")
    c2 = Chromosome(code="01010101")
    assert repr(c1) == repr(c2)
    assert str(c1) == str(c2)
    assert repr(c1) == "Chromosome(size=8, code='01010101', criterion='random')"
    assert str(c1) == "01010101"

    empty_c1 = Chromosome(0, criterion="random")
    empty_c2 = Chromosome(0, criterion="random")
    assert empty_c1.code == ""
    assert empty_c2.code == ""
    assert repr(empty_c1) == "Chromosome(size=0, code='', criterion='random')"
    assert repr(empty_c2) == "Chromosome(size=0, code='', criterion='random')"
    assert str(empty_c1) == ""
    assert str(empty_c2) == ""


def test_concatenation():
    """Test for concatenation of chromosomes"""
    c1 = Chromosome(code="0000")
    c2 = Chromosome(code="1111")
    c3 = Chromosome(code="0101")
    empty_c1 = Chromosome(0)

    assert str(concatenate(c1, c2, c3, empty_c1)) == "000011110101"
    assert str(concatenate(c1, c2, c3, empty_c1, reverse=True)) == "010111110000"
    assert concatenate(c1, c2, c3, empty_c1) == c1.concatenate(c2, c3, empty_c1)
    assert concatenate(c1, c2, c3, empty_c1, reverse=True) == empty_c1.concatenate(c3, c2, c1)
