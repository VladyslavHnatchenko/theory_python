"""Function Parameters and Arguments."""


def cylinder(h, r=1):
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return full


figure1 = cylinder(4, 44)
figure2 = cylinder(232)
print(figure1)
print(figure2)

"""Programming Functions."""
# def rectangle():
#     a = float(input("Width: "))
#     b = float(input("Height: "))
#     print("Square: %.2f" % (a*b))
#
#
# def triangle():
#     a = float(input("Base: "))
#     h = float(input("Height: "))
#     print("Square: %.2f" % (0.5*a*h))
#
#
# def circle():
#     r = float(input("Radius: "))
#     print("Square: %.2f" % (3.14 * r**2))
#
#
# figure = input("1-rectangle, 2-triangle, 3-circle: ")
#
# if figure == "1":
#     rectangle()
# elif figure == "2":
#     triangle()
# elif figure == "3":
#     circle()
# else:
#     print("Input Error")


###########################################################

# def count_food():
#     a = int(input())
#     b = int(input())
#     print("Total", a+b, "pieces.")
#
#
# print("How many bananas and pineapples are there for monkeys?")
# count_food()
#
# print("How many bugs and worms for hedgehogs?")
# count_food()
#
# print("How many fish and shellfish are for otters?")
# count_food()
