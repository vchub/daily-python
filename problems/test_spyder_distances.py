import itertools as it

import numpy as np


def sum_it(xs):
    """https://brilliant.org/weekly-problems/2018-06-18/intermediate/?p=4
    norm of vectors sum

    :xs: [[num]]
    :return: num

    """

    ys = xs

    return np.linalg.norm(np.sum(ys, axis=0)), xs


def make_vectors(xs, d):
    return list(map(lambda x: np.array(x) - np.array(d), xs))


def aprox_solution(xs, x_range, y_range):
    points = [
        sum_it(make_vectors(xs, d))
        for d in it.product(range(*x_range), range(*y_range))
    ]
    res = list(filter(lambda x: x[0] < 1, points))

    return res


def test_d():
    # assert sum_it([[3, 4], [1, 2]]) == 5
    # assert list(make_vectors([[3, 4], [1, 2]], [1, 1])) == 5
    # assert aprox_solution([[0, 0], [60, 30], [30, 90]], [0, 60], [0, 90]) == 5
    pass


# print(list(it.accumulate(range(1, 100), lambda acc, n: acc * (1 - n * 0.01))))


def share(s, n, m):
    if n > m:
        return
    got = s * 0.01 * n
    sn = s * (1 - 0.01 * n)
    print(n, got, sn)
    share(sn, n + 1, m)


# share(1, 1, 40)
