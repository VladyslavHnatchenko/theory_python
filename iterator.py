"""Python Iterators."""

x = [1, 2, 3]
y = iter(x)
z = iter(x)
# >>> next(y)
# 1
# >>> next(y)
# 2
# >>>
# >>> next(y)
# 3
# >>> next(y)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> next(z)
# 1
# >>> type(x)
# <class 'list'>
# >>> type(y)
# <class 'list_iterator'>
# >>> type(z)
# <class 'list_iterator'>
# ------------------------------------------------------------------- #

# class SimpleIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
#
# s_iter2 = SimpleIterator(5)
# for i in s_iter2:
#     print(i)

# a = [10, 20, 30, 40]
# for id, item in enumerate(a):
#     a[id] = item + 5
#
# print(a)

# a = [10, 20, 30, 40]
# for i in enumerate(a):
#     print(i)
#
# b = "hello"
# for i in enumerate(b):
#     print(i)
#
# c = {1: 'a', 2: 'b', 3: 'c'}
# for i in enumerate(c):
#     print(i)

# ------------------------------------------------------------------- #
# from random import random
#
# generator2 = (round(random() + 1, 2) for i in range(5))
# for i in generator2:
#     print(i)
#
# print("\n")
#
#
# def random_increase(quantity):
#     cur = 0
#     while quantity > 0:
#         cur += random()
#         quantity -= 1
#         yield round(cur, 2)
#
#
# generator = random_increase(5)
# for i in generator:
#     print(i)

# class RandomIncrease:
#     def __init__(self, quantity):
#         self.qty = quantity
#         self.cur = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.qty > 0:
#             self.cur += random()
#             self.qty -= 1
#             return round(self.cur, 2)
#         else:
#             raise StopIteration
#
#
# iterator = RandomIncrease(5)
# for i in iterator:
#     print(i)

# ------------------------------------------------------------------- #
# a = range(2)
# b = iter(a)
# print(type(a))
# print(type(b))
#
# for i in a:
#     print(i)
#
# for i in a:
#     print(i)
#
# for i in b:
#     print(i)
#
# for i in b:
#     print(i)

# a = {1: 'a', 2: 'b'}
# b = iter(a)
# print(b)
# print(next(b))

# a = [1, 2]
# a = 'hi'
# b = a.__iter__()
# c = b.__iter__()
# print(a)
# print(b)
# print(c)
#
# print(b.__next__())
# print(c.__next__())
# print(b.__next__())  # StopIteration


# a = [1, 2]
# b = a.__iter__()
# print(a)
# print(type(a))
# # print(a.__next__())  # AttributeError: 'list' object has no attribute '__next__'
# print(b)
# print(type(b))
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())  # StopIteration

# ------------------------------------------------------------------- #
# from itertools import islice
#
#
# class Fib:
#     def __init__(self):
#         self.prev = 0
#         self.curr = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.curr
#         self.curr += self.prev
#         self.prev = value
#         return value
#
#
# f = Fib()
# d = Fib()
# print(list(islice(f, 0, 10)))
# print(list(islice(d, 0, 30)))

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
