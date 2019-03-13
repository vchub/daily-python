# Write a function, add_subtract, which alternately adds and subtracts curried
# arguments. Here are some sample operations: add_subtract(7) -> 7
# add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0 add_subtract(-5)(10)(3)(9) -> -5 + 10
# - 3 + 9 -> 11


def add_subtract(init: int = 0):
    add: bool = True
    init = init

    def f(*xs):
        nonlocal add, init
        if not xs:
            return init
        x = xs[0]
        if add:
            init += x
        else:
            init -= x
        add = not add
        return f

    return f


def test_add_subtract():
    assert add_subtract(1)() == 1
    assert add_subtract(1)(2)() == 3
    assert add_subtract(1)(2)(3)() == 0
    assert add_subtract(-5)(10)(3)(9)() == 11
