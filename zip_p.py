"""zip() function in Python."""


values = [1.34, 3.25, 2.99]
coefficient = [3, 2, 2]

for i, j in zip(values, coefficient):
    print(i*j)

# a = [10, 20, 30, 40]
# c = [1.1, 1.2, 1.3, 1.4]
# ac = zip(a, c)
# print(type(ac))
#
# ac = list(ac)
# print(type(ac))
# print(ac)

# import itertools
#
# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']
# c = [1.1, 1.2]
#
# for i in itertools.zip_longest(a, b, c):
#     print(i)

# ------------------------------------------------------------------- #

# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']
#
# for i in zip(a, b):
#     print(i, type(i))

# for i, j in zip(a, b):
#     print(i, j)
