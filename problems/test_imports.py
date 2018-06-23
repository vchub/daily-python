import math as m

import numpy.random as rnd

m.log(5)

# print('this is math: {}'.format(type(math)))
# dir(math)
# 'pi to 4 sig digits: {:.4}'.format(math.pi)
# math.log(32,2)
# help(math.log)
#
# roll = rnd.randint(low=1, high=6, size=10)
# roll
# dir(roll)
# type(roll)
# roll.mean()
# roll.var()
# roll <= 3
# s = '23x1'
# '2355'.isnumeric()


def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    n = height // 2
    top = [' ' * (n - i) + '/' * i + '\\' * i for i in range(1, n + 1)]
    botton = [' ' * (n - i) + '\\' * i + '/' * i for i in range(n, 0, -1)]

    return '\n'.join(top) + '\n' + '\n'.join(botton)


# def test_diamond():
#     print(diamond(2))
#     print(diamond(4))
#     print(diamond(8))


def make_fr(history):
    fr = {}

    for i in range(len(history) - 1):
        cur = history[i]
        nxt = history[i + 1]

        if cur not in fr:
            fr[cur] = {}

        if nxt in fr[cur]:
            fr[cur][nxt] += 1
        else:
            fr[cur][nxt] = 1

    return fr


def conditional_roulette_probs(history):
    """

    Example:
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5},
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """

    fr = make_fr(history)
    # prob = {k: fr[k] / sum(fr[k].values()) for k in fr}
    prob = {}

    for k, v in fr.items():
        n = sum(v.values())
        prob[k] = {}

        for k1, v1 in v.items():
            prob[k][k1] = v1 / n

    return prob


def test_cond():
    # print(conditional_roulette_probs([1, 3, 1, 5, 1]))
    assert conditional_roulette_probs([1, 3, 1, 5, 1]) == {
        1: {
            3: 0.5,
            5: 0.5
        },
        3: {
            1: 1
        },
        5: {
            1: 1
        }
    }
