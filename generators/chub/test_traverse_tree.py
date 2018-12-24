from dataclasses import dataclass
from typing import Any, Generator, Iterator, List

import pytest

E = int


@dataclass
class Node(object):
    v: E
    l: Any = None
    r: Any = None


def add(x: Node, v: E) -> Node:
    if not x:
        return Node(v)
    if v < x.v:
        x.l = add(x.l, v)
    if v > x.v:
        x.r = add(x.r, v)
    return x


def inorder(node: Node) -> Iterator[E]:
    if node:
        for x in inorder(node.l):
            yield x
        yield node.v
        for x in inorder(node.r):
            yield x


def test():
    root = Node(0)
    N = 3
    for i in range(N):
        root = add(root, i)
    assert list(inorder(root)) == list(range(N))


def xtest_busting_recursion():
    def busting(N):
        root = Node(0)
        for i in range(N):
            root = add(root, i)

    with pytest.raises(RecursionError) as err:
        busting(1000)
    assert 'maximum recursion depth' in str(err.value)
