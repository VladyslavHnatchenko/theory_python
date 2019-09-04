import math
from decorators import do_twice, debug


math.factorial = debug(math.factorial)


def appriximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


appriximate_e(5)


# ------------------------------------------------------------------- #
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
#
#
# print(return_greeting("Adam"))

# ------------------------------------------------------------------- #
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("John")

# ------------------------------------------------------------------- #
# @do_twice
# def say_whee():
#     print("Whee!")
#
#
# say_whee()
