"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    # if len(list_one) == 0 and len(list_two) == 0:
    #     return EQUAL

    str_one = '-'.join([str(i) for i in list_one])
    str_two = '-'.join([str(i) for i in list_two])

    if len(list_one) < len(list_two):
        if str_one in str_two:
            return SUBLIST

    if len(list_one) > len(list_two):
        if str_two in str_one:
            return SUPERLIST

    if str_one == str_two:
        return EQUAL

    return UNEQUAL


# def is_sub(list_one, list_two):
#     str_one = list_one.join()
#     str_two = list_two.join()

#     return str_one in str_two

    # if len(list_two) < len(list_one):
    #     return False

    # for index_two in range(len(list_two)):
    #     if test(list_one, list_two, index_two):
    #         return True

    # return False


# def test(list_one, list_two, index_two):
#     border = len(list_two) - index_two

#     for index_one in range(len(list_one)):
#         if index_one >= border:

#             return False

#         if list_one[index_one] != list_two[index_two]:
#             return False

#         index_two += 1

#     return True
