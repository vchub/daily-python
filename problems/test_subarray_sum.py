# pylint: disable=invalid-name,missing-docstring,c0330

# https://leetcode.com/problems/subarray-sum-equals-k/description/

# return sub_sum(nums, k)


def arr_sum(xs):
    """[int], i, j -> sum(xs[i:j])
    """
    cache = {}

    def fn(i, j):
        key = (i, j)

        return cache[key] if key in cache else cache.setdefault(
            key, sum(xs[i:j]))

    return fn


def sub_sum(xs, k):
    """[int], int -> int
    number of continuous sub-arrays which sum = k
    """
    # csum = arr_sum(xs)

    n = len(xs)
    i = 0
    cnt = 0

    while i < n:
        csum = 0

        for j in range(i, n):
            # csum = sum(xs[i:j])
            csum += xs[j]

            if csum == k:
                cnt += 1

                if j < (n - 1) and xs[j + 1] != 0:
                    break

        i += 1

    return cnt


import collections
import csv
import os
import timeit


def sub_sum2(xs, k):
    count = collections.Counter()
    count[0] = 1
    ans = su = 0

    for x in xs:
        su += x
        ans += count[su - k]
        count[su] += 1

    return ans


def run_big():
    """ """
    # print('pwd', os.getcwd())

    f_name = os.path.abspath('./leetcode_try/tests/sub_array_sum_tc.txt')
    with open(f_name) as f:
        reader = csv.reader(f, delimiter=',')

        xs = list(map(int, next(reader)))
        # print(xs)

        return sub_sum2(xs, -93)


# t = timeit.timeit('run_big()', globals=globals(), number=1)
# print("time", t)

#
#


def test_sub_sum2():
    """testing
    """
    assert sub_sum2([1], 0) == 0
    assert sub_sum2([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0) == 55
    assert sub_sum2([-77, 74, -54, -24, -50, 62, -18, 89, 75, 54, -31],
                    100) == 1
    assert sub_sum2([3, 2, 1, 100, 1, 2, 3, 4], 6) == 2
    assert sub_sum2([100, 1, 2, 3, 4], 6) == 1
    assert sub_sum2([-1, -1, 1], 0) == 1
    assert sub_sum2([1, 2, 3], 3) == 2
    assert sub_sum2([1, 1, 1], 1) == 3
    assert sub_sum2([1, 1, 1], 2) == 2
    assert sub_sum2([1, 2, 1], 1) == 2
    assert sub_sum2([1, 2, 1], 3) == 2
    assert sub_sum2([1, 2, 1, -1, 2], 1) == 3


def test_sub_sum():
    """testing
    """
    assert sub_sum([1], 0) == 0
    assert sub_sum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0) == 55
    assert sub_sum([-77, 74, -54, -24, -50, 62, -18, 89, 75, 54, -31],
                   100) == 1
    assert sub_sum([3, 2, 1, 100, 1, 2, 3, 4], 6) == 2
    assert sub_sum([100, 1, 2, 3, 4], 6) == 1
    assert sub_sum([-1, -1, 1], 0) == 1
    assert sub_sum([1, 2, 3], 3) == 2
    assert sub_sum([1, 1, 1], 1) == 3
    assert sub_sum([1, 1, 1], 2) == 2
    assert sub_sum([1, 2, 1], 1) == 2
    assert sub_sum([1, 2, 1], 3) == 2
    assert sub_sum([1, 2, 1, -1, 2], 1) == 3


def scan_arr(xs, k):
    """[int], int -> int
    """

    # if len(xs) < 1:
    #     return 0
    #
    # min_xs = min(xs)
    #
    # if min_xs < 0:
    #     xs = [x - min_xs for x in xs]
    #     k -= min_xs

    cnt = 0
    start = 0
    total = 0
    # neg_start = 0
    # neg_sum = 0

    for ind, x in enumerate(xs):
        total += x

        if total > k:
            while total > k and start < ind:
                total -= xs[start]
                start += 1

        # if total < k:
        #     while total < k and neg_start < ind:
        #         total -= xs[neg_start]
        #         neg_start += 1

        if total == k:
            cnt += 1
            total -= xs[start]
            start += 1

    return cnt


def two_scan(xs, k):
    """[int], int -> int
    """

    forward = scan_arr(xs, k)
    b = xs[:]
    b.reverse()
    back = scan_arr(b, k)

    return max(forward, back)


def xtest_two_scan():
    """testing
    """
    assert two_scan([1], 0) == 0
    assert two_scan([-77, 74, -54, -24, -50, 62, -18, 89, 75, 54, -31],
                    100) == 1
    assert two_scan([3, 2, 1, 100, 1, 2, 3, 4], 6) == 2
    assert two_scan([100, 1, 2, 3, 4], 6) == 1
    assert two_scan([-1, -1, 1], 0) == 1
    assert two_scan([1, 2, 3], 3) == 2
    assert two_scan([1, 1, 1], 1) == 3
    assert two_scan([1, 1, 1], 2) == 2
    assert two_scan([1, 2, 1], 1) == 2
    assert two_scan([1, 2, 1], 3) == 2
    assert two_scan([1, 2, 1, -1, 2], 1) == 3


def xtest_scan():
    """testing
    """
    assert scan_arr([1], 0) == 0
    assert scan_arr([100, 1, 2, 3, 4], 6) == 1
    assert scan_arr([-1, -1, 1], 0) == 1
    assert scan_arr([1, 2, 3], 3) == 2
    assert scan_arr([1, 1, 1], 1) == 3
    assert scan_arr([1, 1, 1], 2) == 2
    assert scan_arr([1, 2, 1], 1) == 2
    assert scan_arr([1, 2, 1], 3) == 2
    assert scan_arr([1, 2, 1, -1, 2], 1) == 3
