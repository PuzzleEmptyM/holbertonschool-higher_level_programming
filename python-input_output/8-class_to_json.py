#!/usr/bin/python3
""" class_to_json module """


def class_to_json(obj):
    """ returns dictionary description of object """
    return obj.__dict__
