# https://brilliant.org/practice/rule-of-sum-and-rule-of-product-problem-solving/?p=2

import itertools as it

# xs = [
#     list(
#         it.combinations_with_replacement(
#             it.chain([10] * 8, [100] * 5, [500] * 2), i))
#     for i in range(1, 16)
# ]
#
# xs

a = [8] * 5
list(it.chain([8] * 3, [10] * 2))
sum(it.chain([8] * 3, [10] * 2))
