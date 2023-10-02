#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class, inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an arg to each attribute """
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        else:
            for idx, item in enumerate(args):
                if idx == 0:
                    self.id = item
                if idx == 1:
                    self.size = item
                if idx == 2:
                    self.x = item
                if idx == 3:
                    self.y = item

    def __str__(self):
        """ Override the string representation of Square instances """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
