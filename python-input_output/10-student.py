#!/usr/bin/python3
""" module containing definition of Student class """


class Student:
    """ Student class containing first_name, last_name, & age """
    pass

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(entry) is str for entry in attrs):
            attr_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    attr_dict[key] = getattr(self, key)
            return attr_dict
        else:
            return self.__dict__
