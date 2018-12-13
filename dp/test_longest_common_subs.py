# https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0

import functools
import timeit


@functools.lru_cache(maxsize=None)
def lcs(a, b):
    """ str, str -> num """

    if len(a) == 0 or len(b) == 0:
        return 0
    dab = 0

    if a[0] == b[0]:
        dab = lcs(a[1:], b[1:]) + 1

    da = lcs(a[1:], b)
    db = lcs(a, b[1:])

    return max(da, db, dab)


def lcs_tab(a, b):
    """ str, str -> num """

    if len(a) == 0 or len(b) == 0:
        return 0

    m, n = len(a) + 1, len(b) + 1
    tbl = [[None] * n for x in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                tbl[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1] + 1
            else:
                tbl[i][j] = max(tbl[i - 1][j - 1], tbl[i - 1][j],
                                tbl[i][j - 1])

    return tbl[m - 1][n - 1]


def xtest_lcs():
    a = 'ab'
    b = 'a'
    assert lcs(a, b) == 1
    assert lcs_tab(a, b) == 1

    a = 'ab'
    b = 'ab'
    assert lcs(a, b) == 2
    assert lcs_tab(a, b) == 2

    a = 'abcdefglkmxyz'
    b = '_____bdfabckyxxxxz'
    assert lcs(a, b) == 6
    print('lru_cache(): ', lcs.cache_info())
    print('time lsc: ', timeit.timeit(lambda: lcs(a, b), number=100))
    assert lcs_tab(a, b) == 6
    print('time lsc_tab: ', timeit.timeit(lambda: lcs_tab(a, b), number=100))


def run():
    cases = int(input())

    for _ in range(cases):
        x, y = map(int, input().strip().split(' '))
        a = input()
        b = input()
        print(lcs(a, b))


if __name__ == '__main__':
    run()
