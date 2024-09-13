#!/usr/bin/python3
""""
     Prints a square of '#' characters with the given size.
"""


def print_square(size):

    """
    Parameters:
        size (int): The size of the square to print.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)
