"""Array Data Structures in Python"""

"""array.array – Basic Typed Arrays"""
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])
print(arr)

arr[1] = 23.0
print(arr)

del[arr[2]]
print(arr)

arr.append(42.8)
print(arr)

try:
    arr[1] = 'hello'
except TypeError as e:
    print(e)
# ------------------------------------------------------------------- #
"""bytearray – Mutable Arrays of Single Bytes"""

# arr = bytearray((0, 1, 2, 3))
# print(arr)
# print(arr[1])
#
# arr[1] = 27
# print(arr)
#
# del(arr[2])
# print(arr)
#
# arr.append(43)
# print(arr)
#
# try:
#     arr[1] = "hello"
# except TypeError as e:
#     print(e)
#
# try:
#     arr[2] = 300
# except ValueError as e:
#     print(e)
#
# print(bytes(arr))


# ------------------------------------------------------------------- #
"""bytes – Immutable Arrays of Single Bytes"""

# arr = bytes((0, 1, 2, 3))
# print(arr[1])
# print(arr)
#
# try:
#     print(bytes((0, 300)))
# except ValueError as e:
#     print(e)
#
# try:
#     arr[1] = 23
# except TypeError as e:
#     print(e)
#
# try:
#     del(arr[1])
# except TypeError as e:
#     print(e)