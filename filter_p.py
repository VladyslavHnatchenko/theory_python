"""Filter() function - filtering sequences in Python."""


def numbs(x):
    if '0' <= x <= '9':
        return 1
    else:
        return 0


s = "5a 3 k 99 d00"
for i in filter(numbs, s):
    print(i)


# ------------------------------------------------------------------- #
# s = ['a', '', 'd', 'cc', ' ']
# ss = list(filter(None, s))
# print(ss)
#
# a = [-1, 0, 1, 0, 0, 1, 0, -1]
# b = list(filter(None, a))
# print(b)
# ------------------------------------------------------------------- #
# a = [1, -4, 6, 8, -10]
#
#
# def func(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
#
#
# b = filter(func, a)
# b = list(b)
# print(b)
