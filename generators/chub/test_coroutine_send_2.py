from typing import Iterator


def grep(pattern, sink: Iterator) -> Iterator:
    # print(f'\nlooking for {pattern}')
    while True:
        line = yield
        print('line: ', line)
        if pattern in line:
            sink.send(line)
            # print(line)
            # st.append(line)
            # yield line


def sink() -> Iterator:
    while True:
        x = yield
        yield x


def test0():
    gr_sink = sink()
    gr = grep('foo', gr_sink)
    next(gr)
    next(gr_sink)

    ss = ['me bar', 'me foo', 'safool', 'foo', 'foo2']
    _ = (x for x in (gr.send(l) for l in ss))
    # print(list(got))
    # for l in ss:
    #     gr.send(l)
    # got = list(x for x in gr_sink)
    # print(list(got))


# def test1():
#     st = [[]]
#     gr = grep('me', st)
#     next(gr)
#     ss = ['me bar', 'me foo', 'safool']
#     got = (x for x in (gr.send(l) for l in ss))
#     print(list(got))
#     print(st)
