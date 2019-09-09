"""Works with files in python."""

l_ = ["tree", "four"]
f2 = open("data.txt", "w")
f2.write("one")
f2.write("two")
f2.writelines(l_)

f2.close()
print(f2.closed)

f3 = open("data.txt")
print(f3.read())


# f1 = open("data.txt")
#
# for i in open("data.txt"):
#     print(i)

# print(f1.readlines())

# print(f1.read(10))
# print(f1.read())
# print(type(f1.read()))
#
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
