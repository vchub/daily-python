from dataclasses import dataclass
from typing import Any, Generator, Iterator, List

import pytest

E = int


@dataclass
class Node(object):
    v: E
    l: Any = None
    r: Any = None


def add1(x: Node, v: E) -> None:
    t = x
    while x and v < x.v:
        x, t = x.l, x
    while x and v > x.v:
        x, t = x.r, x
    if not x:
        if v < t.v:
            t.l = Node(v)
        else:
            t.r = Node(v)


def add(x: Node, v: E) -> Node:
    if not x:
        return Node(v)
    if v < x.v:
        x.l = add(x.l, v)
    if v > x.v:
        x.r = add(x.r, v)
    return x


def inorder_iter(node: Node) -> Iterator:
    # https://github.com/python/cpython/blob/3.6/Lib/test/test_generators.py
    st = []
    while node:
        while node.l:
            st.append(node)
            node = node.l
        yield node.v
        while not node.r:
            try:
                node = st.pop()
            except IndexError as e:
                return
            yield node.v

        node = node.r


def inorder_recur(node: Node) -> Generator[E, E, None]:
    if not node:
        return
    for x in inorder_recur(node.l):
        yield x
    yield node.v
    for x in inorder_recur(node.r):
        yield x


def test_inorder_iter():
    N = 3
    root = Node(0)
    for i in range(N):
        add1(root, i)
    assert list(inorder_iter(root)) == list(range(N))

    # N = 1000
    # root = Node(0)
    # for i in range(N):
    #     add1(root, i)
    # assert list(inorder_iter(root)) == list(range(N))


def test():
    root = Node(0)
    N = 3
    for i in range(N):
        root = add(root, i)
    assert list(inorder_recur(root)) == list(range(N))


def test_add1():
    N = 3
    root = Node(0)
    for i in range(N):
        add1(root, i)
    assert list(inorder_recur(root)) == list(range(N))


def xtest_busting_recursion():
    def busting(N):
        root = Node(0)
        for i in range(N):
            root = add(root, i)

    with pytest.raises(RecursionError) as err:
        busting(1000)
    assert 'maximum recursion depth' in str(err.value)
