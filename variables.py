"""Local and global variables."""

result = 0


def rectangle():
    a = float(input("Width: "))
    b = float(input("Height: "))
    global result
    result = a * b


def triangle():
    a = float(input("Base: "))
    h = float(input("Height: "))
    global result
    result = 0.5 * a * h


figure = input("1-rectangle, 2-triangle: ")

if figure == "1":
    rectangle()
elif figure == "2":
    triangle()
print("Square: %.2f" % result)
