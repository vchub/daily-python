# https://itnext.io/dynamic-programming-vs-divide-and-conquer-2fea680becbe


def edit_dist_dp(s1, s2):
    """min edit distance
    str, str -> num """
    n, m = len(s1) + 1, len(s2) + 1
    dp = [[0 for x in range(m)] for x in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1])

    return dp[n - 1][m - 1]

    # print(dp)

    # if n == 0: return m
    #
    # if m == 0: return n
    #
    # if s1[0] == s2[0]: return edit_dist_dp(s1[1:], s2[1:])
    #
    # return 1 + min(
    #     edit_dist_dp(s1[1:], s2), edit_dist_dp(s1, s2[1:]),
    #     edit_dist_dp(s1[1:], s2[1:]))


def xtest_edit_dist_dp():
    assert edit_dist_dp('', '') == 0
    assert edit_dist_dp('a', 'a') == 0
    assert edit_dist_dp('a', 'b') == 1
    assert edit_dist_dp('me', 'my') == 1
    assert edit_dist_dp('sunday', 'saturday') == 3
    print(
        'edit_dist_dp("sundayabc", "saturdayefg")',
        timeit.timeit(
            lambda: edit_dist_dp("sundayabc", "saturdayefg"), number=1))


def min_dist(s1, s2):
    """min edit distance
    :a: str
    :b: str
    :return: num
    """
    a, b = splice_on_first_diff(s1, s2)

    if len(a) == 0 or len(b) == 0:
        return max(len(a), len(b))

    ins = min_dist(a[1:], b) + 1
    dels = min_dist(a, b[1:]) + 1
    ch = min_dist(a[1:], b[1:]) + 1

    return min(ins, dels, ch)


import functools
import timeit


@functools.lru_cache(maxsize=None)
def min_dist_cached(s1, s2):
    return min_dist(s1, s2)


# min_dist_cached('abc', 'efg')


def xtest_cached():
    assert min_dist_cached('sunday', 'saturday') == 3
    # print(
    #     'min_dist_cached: ',
    #     timeit.timeit(
    #         lambda: min_dist_cached("catcatcat", "cutcutcut"), number=1))
    print(
        'min_dist_cached("sundayabc", "saturdayefg")',
        timeit.timeit(
            lambda: min_dist_cached("sundayabc", "saturdayefg"), number=1))
    print(min_dist_cached.cache_info())


def xtest_min_dist():
    assert min_dist('a', 'b') == 1
    assert min_dist('me', 'my') == 1
    assert min_dist('kitten', 'sitting') == 3

    assert min_dist('cat', 'cut') == 1
    assert min_dist('geek', 'gesek') == 1
    assert min_dist('sunday', 'saturday') == 3


def splice_on_first_diff(a, b):
    if len(a) == 0 or len(b) == 0:
        return a, b

    if a[0] == b[0]:
        return splice_on_first_diff(a[1:], b[1:])
    else:
        return a, b


def test_splice():
    assert ('', '') == splice_on_first_diff('', '')
    assert ('a', 'b') == splice_on_first_diff('a', 'b')
    assert ('a', 'b') == splice_on_first_diff('aa', 'ab')
    assert ('', 'ab') == splice_on_first_diff('', 'ab')
    assert ('ut', 'at') == splice_on_first_diff('cut', 'cat')
    assert min(1, 2, 3) == 1


@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def test_fib():
    assert [fib(n) for n in range(16)] == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
    ]
    # check cache missed - new numbers
    assert fib.cache_info()[1] == 16
    # print(fib.cache_info())


(1 - 5**.5) / 2
x = 12
x**2 - 7 * x - 60

tuple('python')
list('python')
'python' [::-1]
list(reversed('python'))


def compose(*functions, arg):
    """functions composition"""

    return functools.reduce(lambda acc, f: f(acc), functions, arg)


def test_compose():
    add1 = lambda x: x + 1
    mult2 = lambda x: x * 2
    assert 2 == compose(add1, arg=1)
    assert 3 == compose(add1, add1, arg=1)
    assert 6 == compose(add1, add1, mult2, arg=1)
