#!/usr/bin/python3
"""
This module defines a `Rectangle` class that provides functionality to create
rectangular objects, calculate their area, perimeter, and print their shape
in a console-friendly way.

Classes:
    - Rectangle: Defines a rectangle with width
      and height, and includes methods
      to calculate area, perimeter, and print its visual representation.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    ----------
    width : int
        The width of the rectangle (must be a non-negative integer).
    height : int
        The height of the rectangle (must be a non-negative integer).

    Methods:
    -------
    area():
        Returns the area of the rectangle.
    perimeter():
        Returns the perimeter of the rectangle.
    __str__():
        Returns a string representation of the rectangle for printing.
    print():
        Prints the rectangle to the console.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with optional width and height.

        Parameters:
        ----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
        -------
        int
            The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
        -------
        int
            The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        ----------
        value : int
            The width of the rectangle (must be a non-negative integer).

        Raises:
        ------
        TypeError:
            If the width is not an integer.
        ValueError:
            If the width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
        ----------
        value : int
            The height of the rectangle (must be a non-negative integer).

        Raises:
        ------
        TypeError:
            If the height is not an integer.
        ValueError:
            If the height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        -------
        int
            The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        -------
        int
            The perimeter of the rectangle (width + height), or 0 if either
            dimension is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.height ** 2 + self.width ** 2

    def __str__(self):
        """
        Provides a string representation of the
        rectangle using the '#' character.

        Returns:
        -------
        str
            A string representing the rectangle using rows of '#' characters.
            Returns an empty string if either width or height is 0.
        """
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join('#' * self.width for row in range(self.height))

    def print(self):
        """
        Prints the rectangle to the console using the '#' character.

        If either the width or height is 0, it prints an empty line.
        """
        if self.height == 0 or self.width == 0:
            print()
        for row in range(self.height):
            print('#' * self.width)
