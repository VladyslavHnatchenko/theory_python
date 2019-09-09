"""OOP in python."""


class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)

    def __str__(self):
        rect = []
        for i in range(self.h):
            rect.append(self.s * self.w)

        rect = "\n".join(rect)
        return rect


b = Rectangle(10, 3, '*')
print(b)

# ------------------------------------------------------------------- #
# class A:
#     def __init__(self, v1, v2):
#         self.field1 = v1
#         self.field2 = v2
#
#     def __str__(self):
#         return str(self.field1) + "" + str(self.field2)
#
#
# a = A("hi ", "tim")
# print(a)

# class T1:
#     n = 10
#
#     def total(self, n):
#         self.total = int(self.n) + int(n)
#
#
# class T2:
#
#     def total(self, s):
#         self.total = len(str(s))
#
#
# t1 = T1()
# t2 = T2()
# t1.total(45)
# t2.total(45)
# print(t1.total)
# print(t2.total)

# ------------------------------------------------------------------- #
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
#
# class KitchenTable(Table):
#     def __init__(self, l, w, h, p):
#         Table.__init__(self, l, w, h)
#         self.places = p
#
#
# tk = KitchenTable(2, 1.5, 0.7, 10)
# print(tk.places)
# print(tk.width)
#
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
#
# class ComputerTable(DeskTable):
#     def square(self, e):
#         return DeskTable.square(self) - e


# ct = ComputerTable(2, 1, 1)
# print(ct.square(0.3))

# t1 = KitchenTable(2, 2, 0.7)
# t2 = DeskTable(1.5, 0.8, 0.75)
# t3 = KitchenTable(1, 1.2, 0.8)
# t4 = Table(1, 1, 0.5)
#
# print(t1.set_places(4))
# print(t2.square())
# print(t3.square())
# print(t4.square())

# ------------------------------------------------------------------- #
# class Rectangle:
#     def __init__(self, w=0.5, h=1):
#         self.width = w
#         self.height = h
#
#     def square(self):
#         return self.width * self.height
#
#
# rec1 = Rectangle(5, 2)
# rec2 = Rectangle()
# rec3 = Rectangle(3)
# rec4 = Rectangle(h=4)
# print(rec1.square())
# print(rec2.square())
# print(rec3.square())
# print(rec4.square())

# ------------------------------------------------------------------- #
# class Person:
#     def __init__(self, n, s):
#         self.name = n
#         self.surname = s
#
#
# p1 = Person("Sam", "Baker")
# print(p1.name, p1.surname)

# ------------------------------------------------------------------- #
# class Person:
#     def set_name(self, n, s):
#         self.name = n
#         self.surname = s
#
#
# p1 = Person()
# p1.set_name("Bill", "Ross")
# print(p1.name)
# print(p1.surname)
# print(p1.name, p1.surname)

# ------------------------------------------------------------------- #
# class User:
#     def set_name(self, n):
#         self.name = n
#
#     def get_name(self):
#         try:
#             return self.name
#         except:
#             print("No name")
#
#
# first = User()
# second = User()
# first.set_name("Bob")
# print(first.get_name())
# print(second.get_name())

# ------------------------------------------------------------------- #
# class B:
#     n = 5
#
#     def adder(self, v):
#         return v + B.n
#
#
# l_ = B()
# m_ = B()
# l_.n = 10
# print(l_.n)
# print(l_.adder(3))
# print(m_.adder(4))
#
# l_.test = 'hi'
# print(l_.test)

# ------------------------------------------------------------------- #
