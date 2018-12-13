# "Imagine you have a collection of N wines placed next to each other on a shelf.
# For simplicity, let's number the wines from left to right as they are standing
# on the shelf with integers from 1 to N, respectively. The price of the ith wine
# is pi. (prices of different wines can be different).
# Because the wines get better every year, supposing today is the year 1, on year
# y the price of the ith wine will be y*pi, i.e. y-times the value that current year.
# You want to sell all the wines you have, but you want to sell exactly one wine
# per year, starting on this year. One more constraint - on each year you are all
# owed to sell only either the leftmost or the rightmost wine on the shelf and you are not allowed to reorder the wines on the shelf(i.e. they must stay in the same order as they are in the beginning).
# You want to find out, what is the maximum profit you can get, if you sell the w
# ines in optimal order?"
# So, for example, if the prices of the wines are(in the order as they are place
# d on the shelf, from left to right): p1 = 1, p2 = 4, p3 = 2, p4 = 3. The optimal soluti
# on would be to sell the wines in the order p1, p4, p3, p2 for a total profit 1
# * 1 + 3 * 2 + 2 * 3 + 4 * 4 = 29.

import functools

# from typing import Tuple


def S(xs: list) -> int:
    N = len(xs)

    @functools.lru_cache(None)
    def loop(i, j: int) -> int:
        year = i + N - j
        if i > j:
            return 0
        return max(xs[i] * year + loop(i + 1, j),
                   xs[j] * year + loop(i, j - 1))

    res = loop(0, N - 1)
    # print('lru_cache(): ', loop.cache_info())
    return res


def test_S():
    assert S((1, )) == 1
    assert S((1, 4, 2, 3)) == 29
    assert S((2, 3, 5, 1, 4)) == 50
