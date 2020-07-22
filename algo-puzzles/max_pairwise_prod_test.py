"""
Find the maximum product of two distinct num- bers in a sequence of
non-negative integers.
"""

Num = int


def m_prod0(xs: list) -> Num:
    # a, b, *rest = xs
    # print('rest', rest)
    a, b = xs[:2]
    t = a * b
    for i in range(2, len(xs) - 1):
        for j in range(i, len(xs)):
            if t < xs[i] * xs[j]:
                t = xs[i] * xs[j]

    return t


def test():
    assert m_prod0([1, 2, 3, 4]) == 12
    assert m_prod0([1, -4, 2, 3]) == 6
    assert m_prod0([1, -4, 2, -4, 3]) == 16
