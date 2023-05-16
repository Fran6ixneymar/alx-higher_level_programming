#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Gets all even numbers in a list."""
    even = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even.append(True)
        else:
            even.append(False)

    return (even)
