from typing import Generator, Iterator


def ymap(xs: list, fn) -> list:
    if not xs:
        return
    t = yield ymap(xs[:-1], fn)
    return t.append(fn(xs[0]))


def trampoline():
    xs = [1, 2]

    def fn(x):
        return x + 1

    y = ymap(xs, fn)
    sub = y.send(None)
    res = sub.send(None)
    return res


def send_recieve(n: int) -> Generator[int, int, None]:
    for i in range(n):
        t = yield
        print('t: ', t)
        yield 2 * t


def xtest():
    # print(list(trampoline()))
    sr = send_recieve(5)
    next(sr)
    i = 0
    while i < 5:
        j = sr.send(i)
        print('j: ', j)
        # print(next(sr))
        i += 1
