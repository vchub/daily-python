# Given an array of integers, determine whether it contains a Pythagorean
# triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the
# equation a2+ b2= c2.

import itertools as it
from typing import List


def has_pyth_trian(xs: List[int]) -> bool:
    xs = sorted(set(xs))
    if len(xs) < 3:
        return False
    # xs = filter_less3(xs)
    return any(xs[i]**2 + xs[j]**2 == xs[k]**2 for k in range(2, len(xs))
               for j in range(1, k) for i in range(j))


def filter_less3(xs: List[int]) -> List[int]:
    return xs[:2] + list(xs[i] for i in range(2, len(xs))
                         if xs[i] != xs[i - 1] and xs[i] != xs[i - 2])


def test():
    assert has_pyth_trian([1, 1, 2]) is False
    assert has_pyth_trian([3, 4, 5]) is True
    assert has_pyth_trian([5, 3, 4, 3, 4, 5]) is True
    pythagor_gen = ((a, b, c) for c in ((it.count(3))) for b in range(c)
                    for a in range(b) if a**2 + b**2 == c**2)
    N = 3
    dat = list(it.islice(pythagor_gen, N))
    # print(dat)
    for t in dat:
        assert has_pyth_trian(t) is True
