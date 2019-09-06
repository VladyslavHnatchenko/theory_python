"""Python lists."""

import random

c = []
i = 0
while i < 10:
    c.append(random.randint(0, 100))
    i += 1

print(c)

my_list = ['ab', 'ra', 'ka', 'da', 'bra']
my_list[0:2] = [10, 20]
print(my_list)

b = []
print(b)

a = [12, 3.85, "black", -4]
print(a)
