#!/usr/bin/python3
""" module containing definition of Student class """


class Student:
    """ Student class containing first_name, last_name, & age """
    pass

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
