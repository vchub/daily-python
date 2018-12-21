from typing import Dict, List, Set

E = int
G = Dict[E, List[E]]


def remove_edge(g: G, u, v: E):
    print('removing', g, u, v)
    g[u].remove(v)
    g[v].remove(u)


def have_cycle(g: G) -> bool:
    """Given an undirected graph, determine if it contains a cycle."""
    g = g.copy()
    visited: Set[E] = set()
    u = next(iter(g.keys()))
    st = [u]
    while len(st) > 0:
        u = st.pop()
        if u in visited:
            return True
        visited.add(u)
        for v in g[u]:
            remove_edge(g, u, v)
            st.append(v)
    return False


def test():
    g = {1: []}
    assert have_cycle(g) is False
    g = {1: [2], 2: [1]}
    assert have_cycle(g) is False
    g = {1: [2, 2], 2: [1, 1]}
    assert have_cycle(g) is True
    g = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    assert have_cycle(g) is True
