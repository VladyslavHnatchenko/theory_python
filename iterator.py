"""Python Iterators."""

from itertools import islice


class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


f = Fib()
d = Fib()
print(list(islice(f, 0, 10)))
print(list(islice(d, 0, 30)))


# ------------------------------------------------------------------- #
# class BoundedRepeater:
#     def __init__(self, value, max_repeats):
#         self.value = value
#         self.max_repeats = max_repeats
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count >= self.max_repeats:
#             raise StopIteration
#         self.count += 1
#         return self.value

# ------------------------------------------------------------------- #
# class Repeater:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.value

# ------------------------------------------------------------------- #
# class Repeater:
#     def __init__(self, value):
#         self.value = value
#
#     def __iter__(self):
#         return RepeaterIterator(self)
#
#
# class RepeaterIterator:
#     def __init__(self, source):
#         self.source = source
#
#     def __next__(self):
#         return self.source.value

# ------------------------------------------------------------------- #
# numbers = [1, 2, 3]
# for n in numbers:
#     print(n)
