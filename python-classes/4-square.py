#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides a class `Square` to represent
squares with additional features such as
validating size and calculating the area.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square, which represents
        the length of each side (default is 0).

    Methods
    -------
    area():
        Returns the area of the square.

    Properties
    ----------
    size : int
        Gets or sets the size of the square, with a validation check.
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

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square, calculated as size^2.
        """
        return self.__size**2

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Validates the size to ensure it's a positive integer.

        Parameters
        ----------
        value : int
            The size of the square.

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is negative.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
