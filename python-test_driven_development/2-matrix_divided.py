#!/usr/bin/python3

"""
This module provides a function to divide each
element of a matrix by a given number.

The `matrix_divided` function divides all
elements in a matrix by a specified divisor.
It performs validation on the matrix and the divisor
to ensure they meet the required types and constraints.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a given
    number and returns a new matrix.

    Parameters:
        matrix (list of lists of int/float): The matrix
        to be divided, where each inner list represents a row.
        div (int/float): The divisor by which each
        element of the matrix will be divided.

    Returns:
        list of lists of float: A new matrix with each element
        divided by `div`, rounded to two decimal places.

    Raises:
        TypeError: If `div` is not a number, or if `matrix` is
        not a list of lists of integers or floats,
        or if the rows of the matrix are not all of the same size.
        ZeroDivisionError: If `div` is zero.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix_divided(matrix, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

        >>> matrix_divided([[1, 2], [3, '4']], 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix"
            "(list of lists) of integers/floats"
            )

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
                )

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix"
                    "(list of lists) of integers/floats"
                    )

    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix]

    return new_matrix
