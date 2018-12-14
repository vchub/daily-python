# Given a string consisting of parentheses, single digits, and positive and
# negative signs, convert the string into a mathematical expression to obtain
# the answer.
#
# Don't use eval or a similar built-in parser.
#
# For example, given '-1 + (2 + 3)', you should return 4.


def rm_spaces(s: str) -> str:
    return ''.join(s.split())


def paranthes(exp: str) -> tuple:
    assert exp[0] == '('
    i = 0
    cnt = 1
    while cnt > 0 and i < len(exp):
        i += 1
        if exp[i] == '(':
            cnt += 1
        elif exp[i] == ')':
            cnt -= 1
    return (exp[1:i], exp[i + 1:])


def parse(exp: str) -> tuple:
    if len(exp) < 1:
        return ()
    if exp[0] == '(':
        t1, t2 = paranthes(exp)
        return (parse(t1), ) + parse(t2)
    if exp[0] in '+-0123456789':
        return (exp[0], ) + parse(exp[1:])

    # print(exp)
    raise Exception('can not parse')


def evl(tree: tuple) -> int:
    op1 = {'-': lambda x: -1 * x, '+': lambda x: x}
    op2 = {'-': lambda x, y: x - y, '+': lambda x, y: x + y}
    # print(tree)
    if len(tree) == 0:
        return 0
    if len(tree) == 1:
        if isinstance(tree[0], str) and tree[0] in '0123456789':
            return int(tree[0])
        else:
            return evl(tree[0])
    if isinstance(tree[0], str) and tree[0] in '+-':
        return op1[tree[0]](evl(tree[1])) + evl(tree[2:])

    return op2[tree[1]](evl(tree[0]), evl(tree[2:]))

    # print(tree)
    # raise Exception('can not evaluate ')


def E(s: str) -> int:
    return evl(parse(rm_spaces(s)))


def testE():
    assert E('1') == 1
    assert E('-1') == -1
    assert E('+1') == +1
    assert E('1+1') == 2
    assert E('1   + 1-3 ') == -1
    assert E('1   + 1--3 ') == 5

    assert E('(1)') == 1
    assert E('(1+2)') == 3
    assert E('-(1+2)') == -3
    assert E('-(1+2)+((2))') == -1
    assert E('-4 - (1+2) +(-(2))') == -9
    assert E('-4 - ((-1+2)) +(-(2))') == -7
