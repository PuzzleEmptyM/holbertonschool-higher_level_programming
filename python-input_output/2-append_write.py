#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """ appends input string, returning count of added characters """
    with open(filename, 'a', encoding="utf8") as fayiiil:
        return fayiiil.write(text)
