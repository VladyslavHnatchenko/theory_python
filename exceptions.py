"""Errors and exceptions. Exception Handling."""

# 3.0 example
try:
    n = input("Please enter the number: ")
    n = int(n)
except ValueError:
    print("You are enter not an integer!")
    try:
        3 / 0
    except ZeroDivisionError:
        print("WOW!!! ZeroDivisionError: division by zero")
else:
    print("All OK, you're enter an integer", n)
finally:
    print("The End!")

# 2.0 example
# try:
#     n = input("Please enter the number: ")
#     n = int(n)
# except ValueError:
#     print("You are enter not an integer!")
# else:
#     print("All OK, you're enter an integer", n, ".")
# finally:
#     print("The End!")

# 1.0 example
# n = input("Please enter the number: ")
#
# try:
#     n = int(n)
#     print("Success!)")
# except ValueError:
#     print("You are enter not an integer!")
#     print("Something went wrong!(")
