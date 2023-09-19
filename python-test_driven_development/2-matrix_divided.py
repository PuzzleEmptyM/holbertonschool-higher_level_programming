#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """The function divides all elements of matrix"""

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            else:
                new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix
