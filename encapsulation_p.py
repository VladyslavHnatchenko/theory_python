"""Encapsulation in python."""


class A:
    def __init__(self, v):
        self.field1 = v

    def __setattr__(self, attr, value):
        if attr == "field1":
            self.__dict__[attr] = value
        else:
            raise AttributeError


a = A(15)
print(a.field1)
# print(a.field2)
print(a.__dict__)


# class A:
#     def __init__(self, v):
#         self.field1 = v
#
#
# a = A(10)
# a.field2 = 20
# print(a.field1, a.field2)

# ------------------------------------------------------------------- #
# class DoubleList:
#     def __init__(self, l):
#         self.double = DoubleList.__make_double(l)
#
#     def __make_double(old):
#         new = []
#         for i in old:
#             new.append(i)
#             new.append(i)
#         return new
#
#
# nums = DoubleList([1, 3, 4, 6, 12])
# print(nums.double)
# print(DoubleList.__make_double([1, 2]))

# ------------------------------------------------------------------- #
# class B:
#     __count = 0
#
#     def __init__(self):
#         B.__count += 1
#
#     def __del__(self):
#         B.__count -= 1
#
#     def qty_object():
#         return B.__count
#
#
# a = B()
# b = B()
# print(B.qty_object())


# class B:
#     __count = 0
#
#     def __init__(self):
#         B.__count += 1
#
#     def __del__(self):
#         B.__count -= 1
#
#
# a = B()
# print(B.__count)
# print(B._B__count)

# ------------------------------------------------------------------- #
# class B:
#     count = 0
#
#     def __init__(self):
#         B.count += 1
#
#     def __del__(self):
#         B.count -= 1
#
#
# a = B()
# b = B()
# print(B.count)
# del a
# print(B.count)
# B.count -= 1
# print(B.count)
