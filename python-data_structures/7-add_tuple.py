#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least 2 elements and fill missing elements with 0
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Calculate the sum of the elements in the tuples
    result = (a[0] + b[0], a[1] + b[1])

    return result
