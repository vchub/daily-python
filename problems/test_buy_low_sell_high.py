# https://realpython.com/numpy-array-programming/


def get_running_low_f(x):
    """num -> (num) -> num
    :returns: function providing current min element

    """

    def f(y):
        nonlocal x

        if y < x: x = y

        return x

    return f


def find_dif(xs):
    """[num] -> num """
    f_min = get_running_low_f(xs[0])
    res = 0

    for x in xs:
        d = x - f_min(x)

        if d > res: res = d

    return res


def test_find_dif():
    assert find_dif([1, 1]) == 0
    assert find_dif([1, 2, 3]) == 2
    assert find_dif([1, 2, 3, 0]) == 2
    assert find_dif([1, 2, 3, 0, 3, 5]) == 5
    assert find_dif((20, 18, 14, 17, 20, 21, 15)) == 7


def test_0():
    f = get_running_low_f(1)
    assert f(2) == 1
    assert f(0) == 0
    assert f(1) == 0
