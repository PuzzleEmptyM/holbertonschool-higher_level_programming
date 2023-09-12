#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find multiples of 2 in a list."""
    result = []

    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
