"""Logical expressions and operators."""

a = True
print(type(a))

b = False
print(type(b), "\n")

print(int(a))
print(int(b), "\n")

a = 10
b = 5
c = a == b
print(a + b)
print(a + b > 14)
print(a < 14 - b)
print(a <= b + 5)
print(a != b)
print(a == b)
print(c)
print(a, b, c, "\n")

x = 8
y = 13
print(y < 15 and x > 8)
print(y < 15 or x > 8)
print(not y < 15)
print(not x > 8)
