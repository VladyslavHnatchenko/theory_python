"""The module contains classes of plane figures."""

from math import pi, pow


class Rectangle:
    """Class Rectangle. The constructor accepts length and width."""
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def square(self):
        """Method for calculating the area of a rectangle."""
        return round(self.width * self.height)

    def perimeter(self):
        """Method for calculating the perimeter of a rectangle."""
        return 2 * (self.width + self.height)


class Circle:
    """Class Circle. The constructor takes a radius."""
    def __init__(self, radius):
        self.r = radius

    def square(self):
        """Method for calculating the area of a circle."""
        return round(pi * pow(self.r, 2), 2)

    def length(self):
        """Method for calculating the circumference."""
        return round(2 * pi * self.r)
