"""Sets and Multisets in Python"""

# ---------------------------multiset(bag)--------------------------- #
from collections import Counter

inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)
print(type(inventory))
print(len(inventory))  # Unique elements

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)
print(type(inventory))
print(sum(inventory.values()))  # Total no. of elements

# ---------------------------frozenset------------------------------- #
# vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# print(vowels)
#
# try:
#     vowels.add("p")
# except AttributeError as e:
#     print(e)

# ---------------------------set------------------------------------- #
# vowels = {'a', 'e', 'i', 'o', 'u'}
# print(vowels)
#
# vowels.add('x')
# print(len(vowels))
# vowels.add('e')
# print(len(vowels))
# vowels.add('r')
# print(len(vowels))
# print(vowels)
# assert('e' in vowels)  # Ok
# # assert('z' in vowels)  # AssertionError
#
# squares = {x*x for x in range(10)}
# print(squares)
#
# letters = set('alice')
# print(letters.intersection(vowels))
