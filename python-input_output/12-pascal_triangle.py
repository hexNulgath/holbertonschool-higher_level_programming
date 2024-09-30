#!/usr/bin/python3

"""
This module provides a function to generate Pascal's triangle.

Pascal's triangle is a triangular array of the binomial coefficients,
where the entry at row n and column k is the number of ways to choose
k elements from a set of n elements. Each number is the sum of the
two numbers directly above it in the triangle.

Usage:
    triangle = pascal_triangle(n)
    This will return the first n rows of Pascal's triangle as a list of lists.
"""


def pascal_triangle(n):
    """
    Generate a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists where each list represents a row of the triangle.
              Returns an empty list if n <= 0.
    """
    pascal_list = []

    if n > 0:
        for i in range(n):
            # Create a row with `i + 1` elements initialized to 1
            row = [1] * (i + 1)

            # Calculate the values for the current row
            for j in range(1, i):
                row[j] = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]

            # Append the completed row to the pascal_list
            pascal_list.append(row)

    return pascal_list
