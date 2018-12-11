# Uses python3


def prod(xs):
    """[num] -> num
    find max pairwise product"""

    a = max(xs)
    xs.remove(a)
    b = max(xs)

    return a * b

    # return max(
    #     xs[i] * xs[j] for i in range(len(xs)) for j in range(i + 1, len(xs)))


def test_prod():
    assert prod([1, 2, 3]) == 6
    assert prod([1, 4, 2, 3]) == 12


def run():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    print(prod(a))


if __name__ == '__main__':
    run()

# n = int(input())
# a = [int(x) for x in input().split()]
# assert(len(a) == n)
#
# result = 0
#
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]
#
# print(result)
