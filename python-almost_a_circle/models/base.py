#!/usr/bin/python3
import json
from os.path import isfile

class Base:
    """ Base class initiated """
    __nb_objects = 0

    def __init__(self, id=None):
        """ If id is provided, assign it to the public instance attribute id """
        if id is not None:
            self.id = id
        else:
            """ Otherwise, increment __nb_objects and assign the new value to id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
