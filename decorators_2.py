"""Primer on Python Decorators."""

# import time
# import requests
#
#
# def benchmark(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"[**] Execution time: {end-start} seconds.")
#     return wrapper()
#
#
# @benchmark
# def fetch_webpage():
#     webpage = requests.get("https://google.com")
#
#
# fetch_webpage()


# def decorator_function(func):
#     def wrapper():
#         print('Wrapper function!')
#         print(f'Wrapped function {func}')
#         print('Execution wrapped function')
#         func()
#         print('Exit from wrapper!')
#     return wrapper
#
#
# @decorator_function
# def hello():
#     print("What's up, man!")
#
#
# hello()

def dec(func):
    def func_wrapper():
        print("Before")
        func()
        print("After")
    return func_wrapper


@dec
def hello():
    print("Hello world!")


hello()

# ------------------------------------------------------------------- #
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print("hello!")
#
#
# say_hello()
# ------------------------------------------------------------------- #
# import random
# from datetime import datetime
#
#
# PLUGINS = dict()
#
#
# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func
#
#
# @register
# def say_hello(name):
#     return f"Hello {name}"
#
#
# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
#
# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greeter_func(name)
#
#
# print(PLUGINS)
# print(randomly_greet("Alica"))
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             print(datetime.now())
#             func()
#         else:
#             pass
#     return wrapper
#
#
# def say_whee():
#     print("Whee!")
#
#
# say_whee = not_during_the_night(say_whee)
# say_whee()

# ------------------------------------------------------------------- #
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
#
# def say_whee():
#     print("Hello!")
#
#
# say_whee = my_decorator(say_whee)
# say_whee()
#
#
# def say_by():
#     print("By!")
#
#
# say_by = my_decorator(say_by)
# say_by()

# ------------------------------------------------------------------- #
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child

# ------------------------------------------------------------------- #
# def parent():
#     print("Printing from the parent() function.")
#
#     def first_child():
#         print("Printing from the first_child() function.")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     first_child()
#     second_child()
#
#
# parent()

# ------------------------------------------------------------------- #
# def say_hello(name):
#     return f"Hello {name}"
#
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesome!"
#
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
