# https://www.geeksforgeeks.org/longest-increasing-subsequence/

# import collections
import functools


def get_prev(d, x):
    """{k: v}, x -> (k,v)
    find {k,v} such k < x and v is mas among all such values
    or return the first pair in d
    """

    # ks = filter(lambda y: y < x, d.keys())
    # return max(ks, default=None)
    def f(acc, kv):
        k0, v0 = acc
        k, v = kv

        if k < x and v >= v0:
            return kv
        else:
            return acc

    kv = functools.reduce(f, d.items(), (x, 1))

    return kv


def lis(xs):
    """Longest Increasing Subsequence
    [num] -> num"""

    if len(xs) < 2: return len(xs)
    tbl = {}

    for x in xs:
        k, v = get_prev(tbl, x)

        if k < x:
            tbl[x] = tbl[k] + 1
        else:
            tbl[x] = 1

    return max(tbl.values())


def lis_arr(xs):
    """lis returns length of the longest increasing subsequence in arr of size n"""
    n = len(xs)
    tbl = [1] * n

    for i in range(n):
        for j in range(i):
            if xs[i] > xs[j] and tbl[i] <= tbl[j]:
                tbl[i] = tbl[j] + 1

    return max(tbl, default=0)


def test_lis_arr():
    assert 0 == lis_arr([])
    assert 1 == lis_arr([1])
    assert 1 == lis_arr([3, 2])
    assert 1 == lis_arr([3, 2, 1])
    assert 2 == lis_arr([0, 2, 1])
    assert 2 == lis_arr([0, 0, 2, 1])
    assert 2 == lis_arr([2, 1, 3, 2])
    assert 6 == lis_arr([10, 22, 9, 33, 21, 50, 41, 60, 80])
    assert 4 == lis_arr([50, 3, 10, 7, 40, 80])


def test_lis():
    assert 0 == lis([])
    assert 1 == lis([1])
    assert 1 == lis([3, 2])
    assert 1 == lis([3, 2, 1])
    assert 2 == lis([0, 2, 1])
    assert 2 == lis([0, 0, 2, 1])
    assert 2 == lis([2, 1, 3, 2])
    assert 6 == lis([10, 22, 9, 33, 21, 50, 41, 60, 80])
    assert 4 == lis([50, 3, 10, 7, 40, 80])


# https://www.geeksforgeeks.org/python-count-the-number-of-matching-characters-in-a-pair-of-string/


def matching_chars(a, b):
    """count the number of matching characters
    """

    return len(set(a).intersection(set(b)))


def test_matching_chars():
    assert 0 == matching_chars('', '')
    assert 0 == matching_chars('a', 'b')
    assert 1 == matching_chars('a', 'a')
    assert 2 == matching_chars('acb', 'bxa')
