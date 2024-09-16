#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides a class `Square` to represent
squares with additional features such as
validating size and position, calculating the area,
and printing the square with specific
positioning.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square, which represents
        the length of each side (default is 0).
    position : tuple
        The position of the square, which represents the
        offset when printing the square (default is (0, 0)).

    Methods
    -------
    area():
        Returns the area of the square.

    my_print():
        Prints the square using the '#' character
        with spaces based on the position.

    Properties
    ----------
    size : int
        Gets or sets the size of the square, with a validation check.
    position : tuple
        Gets or sets the position of the square, with a validation check.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square with size and position.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).
        position : tuple, optional
            A tuple of two non-negative integers representing the position
            (default is (0, 0)).

        Raises
        ------
        TypeError
            If size is not an integer or position is
            not a tuple of two positive integers.
        ValueError
            If size is negative.
        """
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(i, int) for i in position) or
                not all(i >= 0 for i in position)):
            raise TypeError("position must be a "
                            "tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        """
        Prints the square using the '#' character.

        The print is offset by the square's
        position attribute. If the size is 0,
        a blank line is printed. The number
        of lines is equal to the size, and each
        line is indented by the position's first element.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns
        -------
        tuple
            The position of the square (horizontal and vertical offset).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Validates the position to ensure it's
        a tuple of two non-negative integers.

        Parameters
        ----------
        value : tuple
            A tuple containing two integers representing the position.

        Raises
        ------
        TypeError
            If position is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a "
                            "tuple of 2 positive integers")
        self.__position = value
