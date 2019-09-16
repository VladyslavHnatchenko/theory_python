"""Mock in Python."""

from itertools import permutations


def real(name):
    if len(name) < 10:
        raise ValueError('String too short to calculate statistics.')

    y = 0
    for i in permutations(range(len(name)), 10):
        y += i
        print(y)
