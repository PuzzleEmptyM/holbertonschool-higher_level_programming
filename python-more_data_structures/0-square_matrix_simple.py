def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []  # Create a new row for the new matrix
        for num in row:
            new_row.append(num ** 2)  # Square value and add to new row
        new_matrix.append(new_row)  # Add new row to new matrix

    return new_matrix
