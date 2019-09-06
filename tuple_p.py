"""Tuple in Python."""

nested = (1, "do", ["param", 10, 20])
print(nested)

nested[2][1] = 15
print(nested)


# ------------------------------------------------------------------- #
def add_num(seq, num):
    new_seq = []
    for i in seq:
        new_seq.append(i + num)
    return new_seq


origin = [3, 6, 2, 6]
changed = add_num(origin, 3)

# print(origin)
# print(changed)

# ------------------------------------------------------------------- #
# def add_num(seq, num):
#     for i in range(len(seq)):
#         seq[i] += num
#     return seq
#
#
# origin = [3, 6, 2, 6]
# changed = add_num(origin, 3)
#
# print(origin)
# print(changed)

# ------------------------------------------------------------------- #
# a = (10, 2.13, "square", 89, 'C')
# print(a)
# print(a[3])
# print(a[1:3])
