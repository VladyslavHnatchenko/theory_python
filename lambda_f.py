"""Lambda Functions in Python."""

# Harmful:
print(list(filter(lambda x: x % 2 == 0, range(16))))

# Better:
list_ = [x for x in range(16) if x % 2 == 0]
print(list_)

# ------------------------------------------------------------------- #
"""
Lexical closure - name for a function that remembers the values from the
enclosing lexical scope even when the program flow is no longer in that scope.
"""


def make_adder(n):
    return lambda x: x + n


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))

# ------------------------------------------------------------------- #
print(sorted(range(-5, 6), key=lambda x: x ** 2))

add = lambda x, y: x + y
print(add(5, 3))
print(add(51, 32))


def add_(x, y):
    return x + y


print(add_(44, 4))

# ------------------------------------------------------------------- #
