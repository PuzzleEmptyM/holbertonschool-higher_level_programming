#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
