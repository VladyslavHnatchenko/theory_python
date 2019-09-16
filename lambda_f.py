"""Lambda Functions in Python."""


add_1 = lambda x: x + 2
print(add_1(7))
print(add_1(19))

# import math
#
#
# def sqroot(x):
#     return math.sqrt(x)
#
#
# print(sqroot(121))
#
# square_rt = lambda x: math.sqrt(x)
# print(square_rt(34))

# from functools import reduce
#
# foo = [2, 13, 33, 32, 222, 43, 78]
#
# print(list(filter(lambda x: x % 3 == 0, foo)))
#
# print(list(map(lambda x: x * 2 + 10, foo)))
#
# print(reduce(lambda x, y: x + y, foo))

# Harmful:
# print(list(filter(lambda x: x % 2 == 0, range(16))))
#
# # Better:
# list_ = [x for x in range(16) if x % 2 == 0]
# print(list_)

# ------------------------------------------------------------------- #
"""
Lexical closure - name for a function that remembers the values from the
enclosing lexical scope even when the program flow is no longer in that scope.
"""


# def make_adder(n):
#     return lambda x: x + n
#
#
# plus_3 = make_adder(3)
# plus_5 = make_adder(5)
#
# print(plus_3(4))
# print(plus_5(4))

# ------------------------------------------------------------------- #
# print(sorted(range(-5, 6), key=lambda x: x ** 2))
#
# add = lambda x, y: x + y
# print(add(5, 3))
# print(add(51, 32))
#
#
# def add_(x, y):
#     return x + y
#
#
# print(add_(44, 4))

# ------------------------------------------------------------------- #
