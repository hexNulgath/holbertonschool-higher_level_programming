#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides a class `Square` to
represent squares with additional features such as
validating size
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square, which represents
        the length of each side (default is 0).
    """
    def __init__(self, size=0):
        """
        Initializes the Square with size and position.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is negative.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
