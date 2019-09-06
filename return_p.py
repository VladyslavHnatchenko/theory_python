"""Return values from a function. Return statement."""


def cylinder():
    r = float(input())
    h = float(input())

    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return side, full


sCyl, fCyl = cylinder()
print("Lateral surface area %.2f" % sCyl)
print("Total area %.2f" % fCyl)

###########################################################
# def cylinder():
#     r = float(input())
#     h = float(input())
#
#     side = 2 * 3.14 * r * h
#     circle = 3.14 * r**2
#
#     full = side + 2 * circle
#     return full
#
#
# print(cylinder())
# square = cylinder()
# print(square)
