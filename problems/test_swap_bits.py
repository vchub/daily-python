# Given an unsigned 8-bit integer, swap its even and odd bits.
# The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped,
# and so on.
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
# Bonus: Can you do this in one line?


def swp(s, shift=1):
    """str -> str"""
    x = int(s, 2)

    return x << shift


def test_swp():
    assert '1' == '{0:b}'.format(1)
    assert '10' == '{0:b}'.format(2)
    assert '10' == '{0:b}'.format(int('010', 2))
    assert '10' == '{0:b}'.format(swp('01'))
    assert '100' == '{0:b}'.format(swp('01', 2))
    assert 4 == swp('1', 2)
    assert 12 == swp('11', 2)
