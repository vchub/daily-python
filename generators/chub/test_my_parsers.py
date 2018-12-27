# Recursive-descent parser code sample, demonstrating a straightforward approach
# followed by CPS conversion.
#
# Grammar:
#
# <expr>    : <term> + <expr>
#             <term>
# <term>    : <factor> * <factor>
#             <factor>
# <factor>  : <number>
#           | '(' <expr> ')'
# <number>  : \d+
#
# Note: our implementation here is simplistic, and suffers from the
# associativity problem described in
# http://eli.thegreenplace.net/2009/03/14/some-problems-of-recursive-descent-parsers/
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.

import re
from typing import Sequence, Tuple

T = str
Num = int
PE = Tuple[Num, Sequence[T]]


def parse_expr(tokens: Sequence[T]) -> PE:
    OP = {'+': lambda a, b: a + b, '-': lambda a, b: a - b}

    lval, tokens = parse_term(tokens)
    if len(tokens) < 2:
        return lval, tokens
    op_t, = tokens[0]
    if op_t in OP.keys():
        rval, tokens = parse_expr(tokens[1:])
        return OP[op_t](lval, rval), tokens
    else:
        return lval, tokens


def parse_term(tokens: Sequence[T]) -> PE:
    OP = {'*': lambda a, b: a * b, '/': lambda a, b: a / b}

    lval, tokens = parse_factor(tokens)
    if len(tokens) < 2:
        return lval, tokens
    op_t, = tokens[0]
    if op_t in OP.keys():
        rval, tokens = parse_term(tokens[1:])
        return OP[op_t](lval, rval), tokens
    else:
        return lval, tokens


def parse_factor(tokens: Sequence[T]) -> PE:
    lval, = tokens[0]
    if lval.isdigit():
        return int(lval), tokens[1:]
    if lval == '(':
        exp, tokens = parse_expr(tokens[1:])
        if tokens[0] != ')':
            raise RuntimeError('should be )')
        return exp, tokens[1:]
    else:
        raise RuntimeError('should be )')


def eval_exp(s: T) -> Num:
    return parse_expr(tokenize(s))[0]


def test():
    assert eval_exp('1') == 1
    assert eval_exp('1+1') == 2
    assert eval_exp('1*2+1') == 3
    assert eval_exp('(2)') == 2
    assert eval_exp('2*( 2 +1) ') == 6
    assert eval_exp('(2 * 3)*( 2 +1) ') == 18
    assert eval_exp('(4/2)*(2 - 3)*( 2 +1) ') == -6
    # TODO:
    assert eval_exp('4/2*(2 - 3)*( 2 +1) ') == -4 / 6


def tokenize(s: str) -> Sequence[str]:
    pattern = r'[0-9.]+|[()*/+-]'
    return tuple(m.group(0) for m in re.finditer(pattern, s))


def test_tokenize():
    assert list(tokenize('1()')) == list('1()')
    assert list(tokenize('2.0')) == ['2.0']
    assert list(tokenize('-2.0')) == ['-', '2.0']
    assert list(tokenize('1+( 2.0*3333 )')) == '1 + ( 2.0 * 3333 )'.split()
