#!/usr/bin/python3
""" introduce area method that raises exception """


class BaseGeometry:
    """ introduce area method that raises exception """

    def area(self):
        """ raises exception due to area not yet implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ verifies that input value for name is integer above zero """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
