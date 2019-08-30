"""Cycles in programming. 'WHILE' and 'FOR'."""

###########################################################
###########################################################

total = 100

i = 0
while i < 5:
    n = int(input())
    total = total - n
    i = i + 1

print("Left", total)

###########################################################

# n = input("Enter the integer number: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Something went wrong!")
#         n = input("Enter the integer number: ")
#
# if n % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
