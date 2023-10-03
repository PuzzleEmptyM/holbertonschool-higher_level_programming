#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initializing constructor """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing class Methods/Attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Setting for size attribute """
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

    def to_dictionary(self):
        """ Function that returns dictionary representation """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """ function to return string """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
