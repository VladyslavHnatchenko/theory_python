"""Branching. Conditional operator."""

old = int(input("Your age: "))
print("Recommendation:", "\n")

if 3 <= old < 6:
    print('"The rabbit in the maze"', "\n")
elif 6 <= old < 12:
    print('"Martian"', "\n")
elif 12 <= old < 16:
    print('"Mysterious Island"', "\n")
elif 16 <= old:
    print('"Mind flow"', "\n")
else:
    print("Your are too young", "\n")

###########################################################
# tovar1 = 50
# tovar2 = 32
#
# if tovar1 + tovar2 > 99:
#     print("Not enough money", "\n")
# else:
#     print("Check paid", "\n")

###########################################################
# b = 0
# a = 50
# n = 98
#
# if n < 100:
#     b = n + a
#
# print(b)
###########################################################
