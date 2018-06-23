def merge(x, y):
    """merge segments

    :x: [num, num]
    :y: [num, num]
    :return: [num, num]

    """

    if x[1] <= y[1]:
        return [x[0], y[1]]
    else:
        return x


def process(xs):
    """merge overlapping segments

    :xs: [[num, num]]
    :xs: [[num, num]]
    :return: TODO

    """
    xs.sort()
    res = []
    cur = xs[0]

    for x in xs[1:]:
        if cur[1] >= x[0]:
            cur = merge(cur, x)
        else:
            res.append(cur)
            cur = x

    res.append(cur)

    return res


def test_merge():
    assert merge([1, 3], [1, 2]) == [1, 3]
    assert merge([1, 3], [1, 3]) == [1, 3]
    assert merge([1, 3], [1, 4]) == [1, 4]


def test_process():
    xs = [[3, 4], [1, 3]]
    exp = [[1, 4]]
    got = process(xs)
    assert got == exp

    xs = [(1, 3), (5, 8), (4, 10), (20, 25)]
    exp = [(1, 3), (4, 10), (20, 25)]
    got = process(xs)
    assert got == exp
