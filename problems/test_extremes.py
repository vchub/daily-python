def test0():
    xs = [1, 0, 2, 2, 3, 1, 2]
    assert get_maxs(xs) == [(1, 0), (3, 4), (2, 6)]


def get_maxs(xs):
    """find maximus of [num]

    :xs: [ind]
    :return: [(m, i)]

    """
    res = [(xs[0], 0)]

    for i in range(1, len(xs) - 1):
        if xs[i] > xs[i + 1] and xs[i] >= xs[i - 1]:
            res.append((xs[i], i))

    if xs[-1] > xs[-2]:
        res.append((xs[-1], len(xs) - 1))

    return res


def get_levels(xs):
    """levels

    :xs: [num]
    :return: [(level, r, l)]

    """
    ms = get_maxs(xs)
    # print('ms:', ms)
    res = []

    for i in range(1, len(ms)):
        [ml, l] = ms[i]
        [mr, r] = max(ms[:i])
        # print('some: ', mr, r, ml, l)
        level = min(mr, ml)
        # check previous leves

        if len(res) > 0 and res[-1][1] == r:
            res.pop()
        res.append((level, r, l))

    return res


def test_get_levels():
    xs = [1, 0, 2, 2, 3, 1, 2]
    assert get_levels(xs) == [(1, 0, 4), (2, 4, 6)]


def fill_xs(xs):
    """find volume

    :xs: [num]
    :return: num

    """
    levels = get_levels(xs)
    # print('levels: ', levels)
    res = []

    for level, r, l in levels:
        # print('--- ', level, l, r)
        pot = 0

        for x in xs[r:l + 1]:
            c = level - x
            pot += c if c > 0 else 0
        res.append(pot)

    # print('res - ', res)

    return sum(res)


def no_test_get_levels():
    xs = [1, 0, 2, 2, 3, 1, 2]
    assert fill_xs(xs) == 2
    xs = [2, 5, 3, 4, 3, 2, 5, 5, 3, 4, 2, 2, 2]
    assert fill_xs(xs) == 9

    xs = [
        4, 2, 4, 1, 5, 3, 16, 6, 17, 19, 4, 13, 5, 3, 10, 10, 13, 6, 2, 1, 5,
        15, 13, 19, 16, 9, 13, 1, 7, 18, 20, 13, 9, 7, 2, 10, 8, 18, 4, 7, 5,
        8, 10, 13, 7, 18, 19, 2, 19, 8, 10, 10, 17, 6, 6, 20, 20, 11, 10, 11,
        13, 9, 7, 1, 10, 5, 12, 16, 10, 7, 15, 13, 12, 10, 1, 1, 4, 2, 16, 10,
        20, 17, 11, 19, 19, 20, 9, 10, 17, 9, 18, 8, 10, 18, 8, 19, 16, 17, 3,
        1
    ]
    assert fill_xs(xs) == 791


def test_f_array():
    """
    This problem was asked by Dropbox.

    What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

    functions = []

    for i in range(10):
        functions.append(lambda : i)

    for f in functions:
        print(f())

    """
    n = 5
    functions = []

    def f(j):
        return lambda: j

    for i in range(n):
        functions.append(f(i))

    res = [x() for x in functions]
    assert res == list(range(n))
