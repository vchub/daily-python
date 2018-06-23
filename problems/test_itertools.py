# https://realpython.com/python-itertools/

import itertools as it
from collections import Counter

list(zip([1, 2, 3], ['a', 'b', 'c']))

iter([1, 2, 3])

list(map(sum, zip([1, 2, 3], [3, 4, 5])))


def test0():
    assert 2 == 2


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n

    return [tuple(inputs[i * n:(i + 1) * n]) for i in range(num_groups)]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
naive_grouper(nums, 2)
nums[1:2]


def better_grouper(inputs, n):
    iters = [iter(inputs)] * n

    return zip(*iters)


ids = [iter(nums)] * 2
ids

list(better_grouper(nums, 2))

# You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills,
# and five $1 dollar bills. How many ways can you make change for a $100 dollar bill?

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

x = {1: 2}

list([k, len(list(g))] for k, g in it.groupby(bills))
freq = Counter(bills)
freq.items()

list((x, y) for x, y in freq.items())


def changes(bills, amount):
    """[num], num -> num

    :bills: [num]
    :return: num

    """

    return count_changes(Counter(bills), amount)


def count_changes(bills, amount):
    """[(num, q-ty)], num -> num

    :bills: [num]
    :return: num

    """

    if amount == 0:
        return 1
    elif len(bills) == 0 and amount != 0:
        return 0
    else:
        res = 0
        [bill, n] = bills.popitem()
        # print(bill, n)

        for i in range(n + 1):
            res += changes(bills, amount - i * bill)

        return res


def test_changes():
    m = [5]
    got = changes(m, 0)
    assert got == 1

    m = [5, 5, 2, 2, 1]
    got = changes(m, 5)
    assert got == 2

    assert changes([10, 5, 5, 2, 2, 1], 10) == 3
    assert changes([20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1],
                   100) == 5


bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
list(it.combinations(bills, 5))


def ch_brute(bills, amount):
    if amount == 0:
        return 1
    ch_100 = set()

    for n in range(1, len(bills)):
        for ch in it.combinations(bills, n):
            if sum(ch) == amount:
                ch_100.add(ch)

    return len(ch_100)


def test_brute():
    assert ch_brute([5], 0) == 1

    assert ch_brute([5, 5, 2, 2, 1], 5) == 2

    assert ch_brute([10, 5, 5, 2, 2, 1], 10) == 3
    assert ch_brute([20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1],
                    100) == 5


def ch_any0(bills, amount):
    """set(num), num -> num

    :bills: set(num)
    :return: num

    """

    bills = set(bills)

    if amount == 0:
        return 1
    elif amount < 0:
        return 0

    if not bills and amount != 0:
        return 0

    full = bills.copy()
    bill = bills.pop()

    a = ch_any0(bills, amount)
    b = ch_any0(full, amount - bill)

    return a + b


def test_ch_any0():
    assert ch_any0([5], 0) == 1

    assert ch_any0(set([5, 2, 1]), 5) == 4
    assert ch_any0(set([50, 20, 10, 5, 1]), 100) == 343


def evens():
    n = 0

    while True:
        yield n
        n += 2


def test_evens():
    assert list(it.takewhile(lambda x: x < 8, evens())) == [0, 2, 4, 6]
    e = evens()
    assert list(next(e) for _ in range(5)) == [0, 2, 4, 6, 8]

    e2 = it.count(step=2)
    assert list(next(e2) for _ in range(5)) == [0, 2, 4, 6, 8]
    odds = it.count(start=1, step=2)
    assert list(next(odds) for _ in range(5)) == [1, 3, 5, 7, 9]


def fibs():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def test_fibs():
    assert list(it.takewhile(lambda x: x < 9, fibs())) == [0, 1, 1, 2, 3, 5, 8]


list(it.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min))
l = [1, 2, 3, 4, 5]
sum(l) / len(l)


def second_order(p, q, r, initial_values):
    """Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
    intermediate = it.accumulate(
        it.repeat(initial_values),
        lambda s, _: (s[1], p * s[1] + q * s[0] + r))

    # print('fkfkfkk-----------------')

    return map(lambda x: x[0], intermediate)


def test_fibs_second_order():
    fibs = second_order(1, 1, 0, (0, 1))
    assert list(next(fibs) for _ in range(7)) == [0, 1, 1, 2, 3, 5, 8]
