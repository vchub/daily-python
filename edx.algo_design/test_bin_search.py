# binary search in ordered array


def biSearch(x, xs):
    """ binary search in ordered array
    """

    def loop(xs, low, up):
        if low > up:
            return None
        pivot = (int)((low + up) / 2)
        if xs[pivot] > x:
            return loop(xs, low, pivot - 1)
        elif xs[pivot] < x:
            return loop(xs, pivot + 1, up)
        return xs[pivot]

    return loop(xs, 0, len(xs) - 1)


def test_biSearch():
    xs = []
    assert biSearch(1, xs) is None
    xs = [1]
    assert biSearch(1, xs) is 1
    assert biSearch(2, xs) is None
    xs = [1, 2, 2, 3, 4, 4]
    assert biSearch(1, xs) is 1
    assert biSearch(2, xs) is 2
    assert biSearch(3, xs) is 3
    assert biSearch(4, xs) is 4
    assert biSearch(0, xs) is None
