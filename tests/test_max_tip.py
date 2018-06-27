import problems.max_tip as p


def xtest_collect_max():
    a = ()
    b = ()
    x, y = 1, 1
    assert p.collect_max(x, y, a, b) == 0
    a = (1, 2)
    b = (2, 1)
    x, y = 1, 1
    assert p.collect_max(x, y, a, b) == 4
    a = (5, 4, 4)
    b = (1, 1, 1)
    n, x, y = len(a), 2, 1
    assert p.collect_max(x, y, a, b) == 10
    a = (5, 4, 4)
    b = (4, 1, 1)
    n, x, y = len(a), 2, 1
    assert p.collect_max(x, y, a, b) == 12

    n, x, y = 8, 4, 4
    a = (1, 4, 3, 2, 7, 5, 9, 6)
    b = (1, 2, 3, 6, 5, 4, 9, 8)
    assert p.collect_max(x, y, a, b) == 43
    print('lru_cache(): ', p.collect_max.cache_info())

    n, x, y = 4, 2, 2
    a = 1, 7, 1, 5
    b = 3, 2, 5, 8
    assert p.collect_max(x, y, a, b) == 21
    print('lru_cache(): ', p.collect_max.cache_info())
