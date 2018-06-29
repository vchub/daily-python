import functools
import operator


def m3(xs):
    assert len(xs) == 3

    return functools.reduce(operator.mul, xs)


def min3(xs):
    """(int) -> (int, int)"""
    assert len(xs) >= 3
    mxs = [m3(xs[i - 1:i + 2]) for i in range(1, len(xs) - 1)]
    min_ind, min_val = min(enumerate(mxs), key=operator.itemgetter(1))

    return min_ind + 1, min_val


# @functools.lru_cache(maxsize=None)
def multop(xs):
    """(int) -> int
    Given an array p[] which represents the chain of matrices such that the
    ith matrix Ai is of dimension p[i-1] x p[i]. We need to write a function
    MatrixChainOrder() that should return the minimum number of multiplications
    needed to multiply the chain.
    """

    if len(xs) < 3: return 0

    if len(xs) == 3: return m3(xs)

    n = len(xs)
    tbl = [[0 for i in range(n)] for i in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            tbl[i][j] = float('inf')

            for k in range(i, j):
                q = tbl[i][k] + tbl[k + 1][j] + xs[i - 1] * xs[k] * xs[j]

                if q < tbl[i][j]:
                    tbl[i][j] = q

    return tbl[1][n - 1]

    # i, min_val = min3(xs)
    # assert i > 0
    # res = multop(xs[0:i] + xs[i + 1::]) + min_val
    # return res

    # res = [
    #     multop(xs[0:i] + xs[i + 1::]) + m3(xs[i - 1:i + 2])
    #     for i in range(1,
    #                    len(xs) - 1)
    # ]
    #
    # return min(res)


def run():
    cases = int(input())

    for _ in range(cases):
        input()
        xs = tuple(map(int, input().strip().split(' ')))
        print(multop(xs))


def test_min3():
    assert 1, 2 == min3((1, 1, 2))
    assert 1, 2 == min3((2, 1, 1))
    assert 2, 20 == min3((10, 5, 1, 4, 5))


def xtest_multop():
    assert 0 == multop((10, 5))
    assert 4500 == multop((10, 30, 5, 60))
    assert 26000 == multop((40, 20, 30, 10, 30))
    assert 6000 == multop((10, 20, 30))
    assert 30000 == multop((10, 20, 30, 40, 30))
    # print('lru_cache: ', multop.cache_info())
    assert 2278 == multop(tuple(range(1, 20)))
    assert 323398 == multop(tuple(range(1, 100)))
    # print('lru_cache: ', multop.cache_info())
