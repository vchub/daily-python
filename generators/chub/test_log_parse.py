import re
from typing import Dict, Iterator

# 81.107.39.38 - - [24/Feb/2008:00:08:59 -0600] "GET ..." 200 7587
# host referrer user [datetime] "request" status bytes

default_pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (\S+) (\S+)" (\S+) (\S+)'


def parse_log_line(lines: Iterator[str],
                   pat: str = default_pattern) -> Iterator[Dict]:
    colnames = ('host', 'referrer', 'user', 'datetime', 'method', 'request',
                'proto', 'status', 'bytes')
    patre = re.compile(pat)
    groups = (patre.match(l) for l in lines)
    tups = (g.groups() for g in groups if g)
    log = (dict(zip(colnames, t)) for t in tups)
    return log


def test0():
    s = '81.107.39.38 - - [24/Feb/2008:00:08:59 -0600] "GET /ply/ply.html HTTP/1.1" 200 7587'

    lines = [s] * 2
    got = list(parse_log_line(lines))
    # print(got)
    assert len(got) == 2
