"""Unit tests for Chromosome"""

import numpy as np

from genus import Chromosome, concatenate


def test_creation():
    """Test the creation of chromosomes"""
    c1 = Chromosome.from_str("01010101")
    c2 = Chromosome(np.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=np.uint8))
    c3 = Chromosome([0, 1, 0, 1, 0, 1, 0, 1])
    assert c1 == c2 == c3
    assert len(c1) == 8
    assert len(c2) == 8
    assert len(c3) == 8
    assert c1.size == 8
    assert c2.size == 8
    assert c3.size == 8

    c1 = Chromosome.from_size(10, criterion="zero")
    c2 = Chromosome.from_size(10, criterion="zero")
    assert c1 == c2
    assert str(c1) == "0000000000"
    assert str(c2) == "0000000000"
    assert len(c1) == 10
    assert len(c2) == 10
    assert c1.size == 10
    assert c2.size == 10

    c1 = Chromosome.from_size(10, criterion="random_binary")
    c2 = Chromosome.from_size(10, criterion="random_binary")
    c1_copy = Chromosome(c1.code)
    c2_copy = Chromosome(c2.code)
    assert c1 == c1_copy
    assert c2 == c2_copy
    assert len(c1) == 10
    assert len(c2) == 10
    assert c1.size == 10
    assert c2.size == 10

    empty_c1 = Chromosome.from_size(0, criterion="random_binary")
    empty_c2 = Chromosome.from_size(0, criterion="random_binary")
    assert str(empty_c1) == ""
    assert str(empty_c2) == ""
    assert empty_c1 == empty_c2
    assert len(empty_c1) == 0
    assert len(empty_c2) == 0
    assert empty_c1.size == 0
    assert empty_c2.size == 0


def test_str():
    """Test strings and repr of chromosomes"""
    c1 = Chromosome.from_str("01010101")
    c2 = Chromosome.from_str("01010101")
    assert repr(c1) == repr(c2)
    assert str(c1) == str(c2)
    assert repr(c1) == "Chromosome(code=array([0, 1, 0, 1, 0, 1, 0, 1], dtype=uint8))"
    assert str(c1) == "01010101"

    empty_c1 = Chromosome.from_size(0, criterion="random_binary")
    empty_c2 = Chromosome.from_size(0, criterion="random_binary")
    assert repr(empty_c1) == "Chromosome(code=array([], dtype=uint8))"
    assert repr(empty_c2) == "Chromosome(code=array([], dtype=uint8))"
    assert str(empty_c1) == ""
    assert str(empty_c2) == ""


def test_concatenation():
    """Test for concatenation of chromosomes"""
    c1 = Chromosome.from_str("0000")
    c2 = Chromosome.from_str("1111")
    c3 = Chromosome.from_str("0101")
    empty_c1 = Chromosome.from_size(0)

    assert str(concatenate(c1, c2, c3, empty_c1)) == "000011110101"
    assert str(concatenate(c1, c2, c3, empty_c1, reverse=True)) == "010111110000"
    assert concatenate(c1, c2, c3, empty_c1) == c1.concatenate(c2, c3, empty_c1)
    assert concatenate(c1, c2, c3, empty_c1, reverse=True) == empty_c1.concatenate(
        c3, c2, c1
    )


def test_split():
    """Test for splitting of chromosomes"""
    c = Chromosome.from_str("000011110011")

    c1 = c.split(4)
    assert str(c1[0]) == "0000"
    assert str(c1[1]) == "11110011"

    c1 = c.split((4, 8, 10))
    assert str(c1[0]) == "0000"
    assert str(c1[1]) == "1111"
    assert str(c1[2]) == "00"
    assert str(c1[3]) == "11"
