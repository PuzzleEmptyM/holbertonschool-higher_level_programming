#!/usr/bin/python3
""" pascal_triangle module """


def pascal_triangle(n):
    """ returns list of integers representing Pascal triangle of size n """
    triangle = []
    if n < 1:
        pass
    else:
        triangle.append([1])
        for row in range(1, n):
            level = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    level.append(1)
                else:
                    prev = triangle[row - 1]
                    level.append(prev[col - 1] + prev[col])
            triangle.append(level)
    return triangle
