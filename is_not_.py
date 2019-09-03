"""The Difference Between “is” and “==” in Python."""

a = [1, 2, 3]
b = a
print(a)
# result [1, 2, 3]
print(b)
# result [1, 2, 3]

print(a == b)
# result True

print(a is b)
# result True

c = list(a)
print(c)
# result [1, 2, 3]
print(a == c)
# result True

print(a is c)
# result False
