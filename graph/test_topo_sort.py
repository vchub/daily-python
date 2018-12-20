# topological sort of DAG directed acyclic graph

from typing import Dict, List

import pytest

E = int
G = Dict[E, List[E]]

# S = float('-inf')
S = -1


def toposort(g: G) -> List[E]:
    status = {k: 'new' for k in g.keys()}

    # attach new source for all vertices
    # g[S] = list(g.keys())

    def dfs(u: E, fn) -> None:
        status[u] = 'active'
        for v in g[u]:
            if status[v] is 'active':
                raise RuntimeError('graph is NOT DAG')
            if status[v] is 'new':
                dfs(v, fn)
        status[u] = 'done'
        # post traverse call
        fn(u)

    st = []

    def tostack(u):
        st.append(u)

    for u in g.keys():
        if status[u] == 'new':
            dfs(u, tostack)

    # dfs(S, tostack)
    # remove S
    # st.pop()
    return list(reversed(st))


def test():
    assert [1, 3, 2, 4, ] == toposort({1: [2, 3], 2: [4], 3: [], 4: []})\

    assert [4, 5, 0, 2, 3, 1] == toposort({
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    })
    with pytest.raises(RuntimeError) as err:
        toposort({1: [2, 3], 2: [1], 3: [], 4: []})
    assert 'NOT DAG' in str(err.value)
