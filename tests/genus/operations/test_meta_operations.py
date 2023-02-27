"""Unit tests for meta operations"""

import genus


def test_sequential():
    """Test the sequential operation"""

    # This is an unintended use case, but it still should be supported
    op = genus.ops.Sequential(
        lambda x: x**2,
        lambda x: 2 * x,
        genus.ops.Identity(),
    )
    assert op(1) == 2
    assert op(2) == 8
    assert op(5) == 50
