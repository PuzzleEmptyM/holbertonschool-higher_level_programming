#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """ reads UTF8 formatted text file, printing to stdout """
    with open(filename, 'r', encoding="utf8") as fillle:
        for line in fillle:
            print(line, end="")
