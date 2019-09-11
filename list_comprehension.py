"""List comprehension in Python."""

# a = {1: 10, 2: 20, 3: 30}
# b = [i*a[i] for i in a]
# print(b)

a = {1: 10, 2: 20, 3: 30}
b = [[i, a[i]] for i in a]
c = []
for i in b:
    for j in i:
        c.append(j)

print(c)

# a = [2, -2.4, -4, 7, 5]
# b = [i**2 for i in a]
# print(b)

# ------------------------------------------------------------------- #
# a = []
# for i in range(1, 15):
#     a.append(i)
#
# print(a)
#
# b = [i for i in range(15, 29)]
# print(b)
