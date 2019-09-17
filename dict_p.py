"""Dictionaries in Python."""

from types import MappingProxyType


read_only = MappingProxyType({'one': 1, 'two': 2})

print(read_only)
print(read_only['one'])

try:
    read_only['one'] = 23
except TypeError as e:
    print(e)
# ------------------------------------------------------------------- #
# from collections import ChainMap
#
#
# dict1 = {'one': 1, 'two': 2}
# dict2 = {'three': 3, 'four': 4}
#
# chain = ChainMap(dict1, dict2)
#
# print(chain)
# print(chain['one'])
# print(chain['three'])
# print(chain['six'])  # KeyError
# print(type(chain))
# ------------------------------------------------------------------- #
# from collections import defaultdict
#
#
# dd = defaultdict(list)
#
# dd['docs'].append('Rafus')
# dd['docs'].append('Kathrin')
# dd['docs'].append('mr Sniffles')
#
# print(dd)
# print(dd['docs'])
# ------------------------------------------------------------------- #
# import collections
#
#
# d = collections.OrderedDict(one=1, two=2, three=3)
# print(d)
#
# d["four"] = 4
# print(d)
# print(d.keys())
# ------------------------------------------------------------------- #

# phone_book = {
#     'bob': 7387,
#     'alice': 3719,
#     'jack': 7052,
# }
#
# squares = {x: x*x for x in range(10)}
#
# print(phone_book)
# print(phone_book['jack'])
# print(squares)
# print(squares[3])

# ------------------------------------------------------------------- #
# animals = {
#     'cat': 1,
#     'dog': 2,
#     'bird': 3,
#     'mouse': 4
# }
#
# print(animals)
#
# for i in animals:
#     print(i)
#
# for d in animals:
#     print(animals[d])
#
# n = animals.items()
# print(n)
#
# for key, value in animals.items():
#     print(key, 'is', value)
