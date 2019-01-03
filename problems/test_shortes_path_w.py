# A competitive runner would like to create a route that starts and ends at his
# house, with the condition that the route goes entirely uphill at first, and
# then entirely downhill.
#
# Given a dictionary of places of the form {location: elevation}, and a
# dictionary mapping paths between some of these locations to their
# corresponding distances, find the length of the shortest route satisfying the
# condition above. Assume the runner's home is location 0.
#
# For example, suppose you are given the following input:
#
# elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
# paths = {
#     (0, 1): 10,
#     (0, 2): 8,
#     (0, 3): 15,
#     (1, 3): 12,
#     (2, 4): 10,
#     (3, 4): 5,
#     (3, 0): 17,
#     (4, 0): 10
# }
# In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a
# distance of 28.

import heapq
from collections import defaultdict
from functools import reduce
from typing import Dict, List, Tuple

G = Dict[int, List[int]]
E = Tuple[int, int]
Paths = Dict[E, int]
Path = List[int]
Elevations = Dict[int, int]


def path_length(paths: Paths, path: Path) -> int:
    return reduce(lambda acc, v: (v, acc[1] + paths[(acc[0], v)]), path[1:],
                  (path[0], 0))[1]


def add_edge(g: G, e: E):
    u, v = e
    g[u].append(v)


def paths_to_graph(paths: Paths) -> G:
    g: G = defaultdict(list)
    for e in paths:
        add_edge(g, e)
    return g


def to_path(g: G, prev: Dict[int, int], start) -> Path:
    res = [start]
    v = prev[start]
    #  TODO: remove #
    i = 100
    while v != start and i > 0:
        i -= 1
        res.append(v)
        v = prev[v]
    res.append(start)
    return list(reversed(res))


def shortest_path(paths: Paths, elev: Elevations, start: int) -> Path:
    """Dijkstra with filtering"""
    g = paths_to_graph(paths)
    # q = list((paths[(start, v)], v) for v in g[start])
    q = [(0, start)]
    prev: Dict[int, int] = {k: k for k in g}
    dist: Dict[int, int] = {k: -1 for k in g}

    def eligible(u, v: int) -> bool:
        p0, p1, p2 = elev.get(prev[u], 0), elev[u], elev[v]
        return (p0 <= p1 <= p1) or (p0 <= p1 and p1 >= p2) or (p0 >= p1 >= p2)

    while q:
        d, u = heapq.heappop(q)
        if u == start and d > 0:
            return to_path(g, prev, u)
        for v in g[u]:
            if eligible(u, v):
                duv = d + paths[(u, v)]
                if duv < dist[v] or dist[v] < 0:
                    dist[v] = duv
                    prev[v] = u
                heapq.heappush(q, (dist[v], v))
    return []


def test():
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10
    }
    elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
    assert path_length(paths, [0, 1, 3]) == 22
    # g = paths_to_graph(paths)
    # print(g)

    got = shortest_path(paths, elevations, 0)
    # print(got)
    assert got == [0, 2, 4, 0]


#
