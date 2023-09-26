#!/usr/bin/python3
""" verifies if input object is of specified input class """


def is_same_class(obj, a_class):
    """ verifies if input object is of specified input class """
    if type(obj) is a_class:
        return True
    else:
        return False
