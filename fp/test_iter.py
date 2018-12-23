import itertools as it


class Naturals(object):
    """Natural numbers"""

    def __init__(self, N):
        """
        :N: range
        """
        self._N = N

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        i = 0
        while i < self._N:
            yield i
            i += 1


def test():
    nat = Naturals(3)
    got = [x for x in nat]
    assert [0, 1, 2] == got
    assert [0, 1, 2] == list(it.islice(Naturals(100), 3))
