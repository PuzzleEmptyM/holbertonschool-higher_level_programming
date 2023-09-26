#!/usr/bin/python3
""" verifies if input object is inherited from input class """


def inherits_from(obj, a_class):
    """ verifies if input object is inherited from input class """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
