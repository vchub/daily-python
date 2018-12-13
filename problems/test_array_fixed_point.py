# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7,
# 8], you should return False.


def a_fix_point(xs: list) -> int:
    i, j = 0, len(xs)
    while i < j:
        pivot = int((i + j) / 2)
        if xs[pivot] < pivot:
            i = pivot
        elif xs[pivot] > pivot:
            j = pivot
        else:
            return pivot
    return None


def test_a_fix_point():
    assert a_fix_point([]) is None
    assert a_fix_point([0]) is 0
    assert a_fix_point([1]) is None
    assert a_fix_point([1, 1]) is 1
    assert a_fix_point([-100, 0, 2, 3]) is 2
    assert a_fix_point([-6, 0, 2, 40]) is 2
    assert a_fix_point([1, 5, 7, 8]) is None
