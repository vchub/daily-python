def f():
    x = 1
    i = 0
    while i < x:
        yield i
        i += 1


def test():
    f.x = 5
    ff = f
    ff.x = 5
    g = ff()
    # g.x = 2
    res = list(x for x in g)
    assert len(res) == 1
