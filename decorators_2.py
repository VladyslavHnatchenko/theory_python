"""Primer on Python Decorators."""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("hello!")

    
say_hello()

# ------------------------------------------------------------------- #
# from datetime import datetime
#
#
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