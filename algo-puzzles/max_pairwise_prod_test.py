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


def m_prod_sort(xs: list) -> Num:
    ys = sorted(xs)
    a, b = ys[:2]
    c, d = ys[-2:]
    if a * b > c * d:
        return a * b
    else:
        return c * d


def m_prod_edges(xs: list) -> Num:
    (a, a1), (b, b1) = get_edges(xs)
    if a * a1 > b * b1:
        return a * a1
    else:
        return b * b1


def get_edges(xs: list) -> tuple:
    """find 2 largest and 2 smallest elements of xs"""
    a1, a = sorted(xs[:2])
    b, b1 = a1, a
    # breakpoint()

    assert a >= a1
    assert b1 >= b

    for i in range(2, len(xs)):
        e = xs[i]
        if e > a:
            a, a1 = e, a
        elif e > a1:
            a1 = e
        elif e < b:
            b, b1 = e, b
        elif e < b1:
            b1 = e

    assert a >= a1
    assert b1 >= b

    return ((a, a1), (b1, b))


def test_m_prod_edges():
    assert m_prod_edges([1, 2, 3, 4]) == 12
    assert m_prod_edges([1, -4, 2, 3]) == 6
    assert m_prod_edges([1, -4, 2, -4, 3]) == 16


def test_get_edges():
    assert get_edges([1, 2, 3, 4]) == ((4, 3), (2, 1))
    assert get_edges([1, 2, -3, 4, -4, -3]) == ((4, 2), (-3, -4))
    assert get_edges([1, 2, -4, -3, 4, -4, -3]) == ((4, 2), (-4, -4))


def test_m_prod_sort():
    assert m_prod_sort([1, 2, 3, 4]) == 12
    assert m_prod_sort([1, -4, 2, 3]) == 6
    assert m_prod_sort([1, -4, 2, -4, 3]) == 16


def test_m_prod0():
    assert m_prod0([1, 2, 3, 4]) == 12
    assert m_prod0([1, -4, 2, 3]) == 6
    assert m_prod0([1, -4, 2, -4, 3]) == 16
