# import itertools as it
from functools import reduce


def counting_sort(xs):
    """https://brilliant.org/wiki/counting-sort/

    :xs: [int]
    :return: [int]

    """

    if not xs:
        return xs
    # O(n)
    c = [0] * (max(xs) + 1)

    # O(n)

    for x in xs:
        c[x] += 1

    # O(n)

    return [x for sublist in collect_c(c) for x in sublist]


def collect_c(c):
    """O(n)"""

    return [[i] * x for i, x in enumerate(c) if x != 0]


def find_longest_seq(xs):
    '''Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

    For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

    Your algorithm should run in O(n) complexity.'''

    def ff(acc, x):
        [gmax, cmax, prev] = acc

        if x - prev == 1:
            return (max(gmax, cmax), cmax + 1, x)
        else:
            return (max(gmax, cmax), 1, x)

    return list(reduce(ff, counting_sort(xs), [0, 1, -2]))[0]

    # m = 0
    # curr = 1
    # prev = -2
    # ys = counting_sort(xs)
    # print(ys)
    #
    # for x in ys:
    #     if x - prev == 1:
    #         curr += 1
    #     else:
    #         if curr > m:
    #             m = curr
    #             curr = 1
    #     prev = x
    #
    # return max(m, curr)


def test_find_longest_seq():
    assert find_longest_seq([100, 4, 200, 1, 3, 2]) == 4
    assert find_longest_seq([5, 100, 4, 200, 1, 3, 2, 6]) == 6


def test_counting_sort():
    assert counting_sort([]) == []
    assert counting_sort([3, 2, 1, 2]) == [1, 2, 2, 3]
    assert counting_sort([4, 0, 3, 2, 1, 2]) == [0, 1, 2, 2, 3, 4]
