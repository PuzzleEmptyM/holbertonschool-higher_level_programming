#!/usr/bin/python3
""" introduce Square subclass of Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square subclass of Rectangle """
    pass

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
