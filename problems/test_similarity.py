# You are given a list of (website, user) pairs that represent users visiting
# websites. Come up with a program that identifies the top k pairs of websites
# with the greatest similarity.
#
# For example, suppose k = 1, and the list of tuples is:
#
# [('a', 1), ('a', 3), ('a', 5), ('b', 2), ('b', 6), ('c', 1), ('c', 2), ('c',
# 3), ('c', 4), ('c', 5) ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('e', 1),
# ('e', 3), ('e': 5), ('e', 6)]
# Then a reasonable similarity metric would most
# likely conclude that a and e are the most similar, so your program should
# return [('a', 'e')].

import heapq
import pdb
from collections import defaultdict
from itertools import combinations, groupby
from operator import itemgetter
from typing import Dict, Iterator, List, Sequence, Set, Tuple

Site = str
User = int
Similarity = int


def similar(sites: Sequence[Tuple[str, int]],
            k: int) -> List[Tuple[Site, Site]]:
    tbl: Dict[Site, Sequence[User]] = {
        k: tuple(v[1] for v in vit)
        for k, vit in groupby(sites, itemgetter(0))
    }

    def cmp(x, y: Site) -> Similarity:
        return -len(set(tbl[x]).intersection(set(tbl[y])))

    cmp_tbl: List[Tuple[Similarity, Tuple[Site, Site]]] = list(
        (cmp(x, y), (x, y)) for x, y in combinations(tbl.keys(), 2))

    heapq.heapify(cmp_tbl)
    # pdb.set_trace()
    res = list(heapq.heappop(cmp_tbl)[1] for i in range(k))
    return res


def test():
    sites = [('a', 1), ('a', 3), ('a', 5), ('b', 2), ('b', 6), ('c', 1),
             ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('d', 4), ('d', 5),
             ('d', 6), ('d', 7), ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
    got = (similar(sites, 3))
    # print(got)
    assert ('a', 'e') in got
