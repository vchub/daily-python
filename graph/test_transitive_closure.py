# A classroom consists of N students, whose friendships can be represented in
# an adjacency list. For example, the following descibes a situation where 0 is
# friends with 1 and 2, 3 is friends with 6, and so on.
#
# {0: [1, 2],
#  1: [0, 5],
#  2: [0],
#  3: [6],
#  4: [],
#  5: [1],
#  6: [3]}
#
# Each student can be placed in a friend group, which can be defined as the
# transitive closure of that student's friendship relations. In other words,
# this is the smallest set such that no student in the group has any friends
# outside this group. For the example above, the friend groups would be {0, 1,
# 2, 5}, {3, 6}, {4}.  Given a friendship list such as the one above, determine
# the number of friend groups in the class.

import collections
from typing import Dict, List, Union

# disjoint-set interface
E = int
V = collections.namedtuple('V', ['parent', 'rank'])
UF = Dict[E, V]
G = Dict[E, List[E]]


def create_uf(xs: List[E]) -> UF:
    return {x: V(None, 1) for x in xs}


def find(uf: UF, e: E) -> E:
    """with path compression"""
    if not uf[e].parent:
        return e
    p = find(uf, uf[e].parent)
    # compression
    uf[e] = V(p, uf[e].rank)
    return p
    # while uf[e].parent:
    #     e = uf[e].parent
    # return e


def union(uf: UF, u: E, v: E) -> UF:
    u = find(uf, u)
    v = find(uf, v)
    if u == v:
        return uf
    if uf[u].rank <= uf[v].rank:
        uf[u] = V(v, uf[u].rank)
        uf[v] = V(None, uf[v].rank + 1)
    else:
        uf[v] = V(u, uf[v].rank)
        uf[u] = V(None, uf[u].rank + 1)
    return uf


def transitive_closure(g: G) -> List[List[E]]:
    """return transitive collections of graph {root: [child]}
    disjoint-set/union-find datastructure application"""
    uf = create_uf(list(g.keys()))
    for u in g.keys():
        for v in g[u]:
            uf = union(uf, u, v)
    # redduce uf to list of closures
    res: dict = collections.defaultdict(list)
    for u, tp in uf.items():
        res[find(uf, u)].append(u)
    return list(res.values())


def test():
    uf = create_uf(list(range(5)))
    assert find(uf, 1) is 1
    uf = union(uf, 1, 2)
    assert uf[1].parent == 2 and uf[1].rank == 1 and uf[2].rank == 2

    g = {1: [2, 3], 2: [3], 3: [], 4: [5], 5: []}
    assert transitive_closure(g) == [[1, 2, 3], [4, 5]]

    g = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
    assert transitive_closure(g) == [[0, 1, 2, 5], [3, 6], [4]]
