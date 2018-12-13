# linked list


class Node():
    """Node"""

    def __init__(self, x):
        """
        :x: object
        :nxt: Node
        """
        self.x = x
        self.nxt = None

    def __str__(self):
        xs = [t.x for t in self]
        return str(xs)

    def __iter__(self):
        t = self
        while (t):
            yield t
            t = t.nxt

    @classmethod
    def fromList(csl, xs) -> 'Node':
        assert xs
        head = node = Node(xs[0])
        for x in xs[1:]:
            node.nxt = Node(x)
            node = node.nxt
        return head

    def insert(self, x) -> 'Node':
        self.last().nxt = Node(x)
        return self

        # def rm(self, x) -> 'Node':
        #     t = None
        #     for t in self:
        #         if t.x == x:
        #             p = t.last()
        #             dddd

        self.last().nxt = Node(x)
        return self

    def last(self) -> 'Node':
        t = None
        for t in self:
            pass
        return t

    def len(self) -> int:
        i = 0
        for _ in self:
            i += 1
        return i


def test_LL():
    # assert Node.fromList([]) is AssertionError

    ls = Node(1).insert(2)
    print(ls)
    assert ls.len() == 2

    ls = Node.fromList([1, 2, 3])
    print(ls)
    assert ls.len() == 3
