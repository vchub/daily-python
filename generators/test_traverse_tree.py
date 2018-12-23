from dataclasses import dataclass
from typing import Any, List

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


def recur_inorder(x: Node) -> List[E]:
    if not x:
        return []
    return recur_inorder(x.l) + [x.v] + recur_inorder(x.r)


def test():
    root = Node(0)
    N = 3
    for i in range(N):
        root = add(root, i)
    assert recur_inorder(root) == list(range(N))

    def busting(N):
        root = Node(0)
        for i in range(N):
            root = add(root, i)

    with pytest.raises(RecursionError) as err:
        busting(1000)
    assert 'maximum recursion depth' in str(err.value)
