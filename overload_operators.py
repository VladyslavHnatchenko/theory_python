"""Overload operators in Python."""


class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)


lesson = Data(
    'class',
    'object',
    'inheritance',
    'polymorphism',
    'encapsulation',
)
mar_ivanna = Teacher()
vasy = Pupil()
pety = Pupil()
mar_ivanna.teach(lesson[2], vasy, pety)
mar_ivanna.teach(lesson[0], pety)
print(vasy.knowledge)
print(pety.knowledge)

# ------------------------------------------------------------------- #
# class A:
#     def __repr__(self):
#         return "It's obj of A"
#
#
# a = A()
# print(a)
# print(repr(a))
# print(str(a))
#

# a = '3 + 2'
# b = repr(a)
# print(a)
# print(b)
# print(eval(a))
# print(eval(b))
#
# c = "Hello\nWorld"
# d = repr(c)
# print(c)
# print(d)

# class A:
#     def __str__(self):
#         return "This's object of A"
#
#
# a = A()
# print(a)
# print(str(a))
# print(repr(a))

# ------------------------------------------------------------------- #
# class Changeable:
#     def __init__(self, color):
#         self.color = color
#
#     def __call__(self, new_color):
#         self.color = new_color
#
#     def __str__(self):
#         return f"{self.color}"
#
#     # def __str__(self):
#     #     return "%s" % self.color
#
#
# canvas = Changeable("green")
# frame = Changeable("blue")
#
# canvas("red")
# frame("yellow")
#
# print(canvas, frame)

# ------------------------------------------------------------------- #
# class A:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __str__(self):
#         return str(self.arg)
#
#
# class B:
#     def __init__(self, *args):
#         self.a_list = []
#         for i in args:
#             self.a_list.append(A(i))
#
#     def __getitem__(self, i):
#         return self.a_list[i]
#
#
# group = B(5, 10, 'abc')
# print(group[0])
# print(group[2])
# print(group.a_list[1])
