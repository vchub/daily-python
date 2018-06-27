# https://practice.geeksforgeeks.org/problems/path-in-matrix/0

import functools


def v_to_m(n, xs):
    M = []

    for i in range(len(xs) // n):
        M.append(tuple(xs[i * n:(i + 1) * n]))

    return tuple(M)


@functools.lru_cache(maxsize=None)
def path(M, r, c):
    """[[num]], r, c -> num
    Starting from [r][c] cell return the largest sum of any
    of the paths up to row N-1."""
    n = len(M)

    if r == n - 1: return M[r][c]
    dl = path(M, r + 1, c - 1) if c > 0 else 0
    d = path(M, r + 1, c)
    dr = path(M, r + 1, c + 1) if c < n - 1 else 0

    return M[r][c] + max(dl, d, dr)


def m_path(M):
    """[[num]]-> num
    Starting from any column in row 0, return the largest sum of any
    of the paths up to row N-1."""
    # print(M)
    cc = [path(M, 0, i) for i in range(len(M))]

    return max(cc)


def test_path():
    assert 6 == m_path(v_to_m(2, (1, 2, 3, 4)))
    xs = (2, 1, 3, 1, 4, 2, 2, 1, 1)
    assert 9 == m_path(v_to_m(3, xs))
    xs = (348, 391, 618, 193)
    assert 1009 == m_path(v_to_m(2, xs))


def test_v_to_m():
    assert ((1, 2), (3, 4)) == v_to_m(2, (1, 2, 3, 4))
    assert ((1, 2, 3), (4, 5, 6),
            (7, 8, 9)) == v_to_m(3, (1, 2, 3, 4, 5, 6, 7, 8, 9))


def run():
    cases = int(input())

    for _ in range(cases):
        n = int(input().strip())
        xs = tuple(map(int, input().strip().split(' ')))
        M = v_to_m(n, xs)
        print(m_path(M))


if __name__ == '__main__':
    run()
