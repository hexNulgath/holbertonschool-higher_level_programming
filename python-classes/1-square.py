#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides a class `Square` to
represent squares with additional features such as
size
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square, which
        represents the length of each side.
    """

    def __init__(self, size):
        """
        Initializes the Square with size

        Parameters
        ----------
        size : int
        """
        self.__size = size
