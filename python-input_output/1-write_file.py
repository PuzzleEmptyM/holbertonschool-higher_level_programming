#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ writes string to text file, returning written characters """
    with open(filename, 'w', encoding="utf8") as fayl:
        return fayl.write(text)
