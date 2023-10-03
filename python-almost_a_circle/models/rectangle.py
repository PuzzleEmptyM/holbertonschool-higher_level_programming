#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class initiated """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor Parameters and Attributes Created """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Setting width return """
        return self.__width

    @width.setter
    def width(self, value):
        """ Initializing characteristics of widh """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Setting height return """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting characteristics of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Setting return for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting characteristics for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ setting return for x """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting characteristics of y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def update(self, *args, **kwargs):
        """ Assigns an arg to each attribute """
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        else:
            for idx, item in enumerate(args):
                if idx == 0:
                    self.id = item
                if idx == 1:
                    self.width = item
                if idx == 2:
                    self.height = item
                if idx == 3:
                    self.x = item
                if idx == 4:
                    self.y = item

    def to_dictionary(self):
        """ Function that returns dictionary representation """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def area(self):
        """ Setting return for area """
        return self.__width * self.__height

    def display(self):
        """ Displays # character for rectangle area """
        for y in range(self.y):
            print()
        for hite in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for wdth in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Function to display rectangle specs """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))
