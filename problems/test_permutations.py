# http://faculty.cse.tamu.edu/djimenez/ut/utsa/cs3343/lecture25.html

import itertools as it


def itp(xs: list) -> list:
    return list(it.permutations(xs))


def perm(xs: list) -> list:
    def _perm(res: list, xs: list, i: int, n: int):
        """generates permutations of xs from elem i to n-1"""
        if i == n:
            res.append(tuple(xs))
        else:
            for j in range(i, n):
                # recursively explore permutations from i to n-1
                # swap i, j
                xs[i], xs[j] = xs[j], xs[i]
                _perm(res, xs, i + 1, n)
                # swap back
                xs[i], xs[j] = xs[j], xs[i]
        return None

    res: list = []
    _perm(res, xs, 0, len(xs))
    return res


def test_perm():
    N = 6
    for i in range(N + 1):
        xs = list(range(i))
        got = sorted(perm(xs))
        exp = itp(xs)
        assert got == exp
