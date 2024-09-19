#!/usr/bin/python3
"""
This module defines a Rectangle class that provides methods for
manipulating rectangle objects. It allows setting and getting
the width and height with appropriate validation, and includes
methods to calculate the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    ----------
    __width : int
        The width of the rectangle (private).
    __height : int
        The height of the rectangle (private).

    Methods:
    -------
    __init__(self, width=0, height=0):
        Initializes the rectangle with optional width and height.

    width(self):
        Retrieves the width of the rectangle.

    width(self, value):
        Sets the width of the rectangle and validates the value.

    height(self):
        Retrieves the height of the rectangle.

    height(self, value):
        Sets the height of the rectangle and validates the value.

    area(self):
        Calculates and returns the area of the rectangle.

    perimeter(self):
        Calculates and returns the perimeter of the rectangle. If either
        width or height is zero, it returns 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with width and height.

        Parameters:
        ----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).

        Raises:
        ------
        TypeError:
            If width or height is not an integer.
        ValueError:
            If width or height is negative.
        """
        self.height = height  # Uses the height setter
        self.width = width  # Uses the width setter

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
        -------
        int
            The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
        -------
        int
            The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle, with validation.

        Parameters:
        ----------
        value : int
            The new width of the rectangle.

        Raises:
        ------
        TypeError:
            If width is not an integer.
        ValueError:
            If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle, with validation.

        Parameters:
        ----------
        value : int
            The new height of the rectangle.

        Raises:
        ------
        TypeError:
            If height is not an integer.
        ValueError:
            If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        -------
        int
            The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        If either width or height is zero, the perimeter is zero.

        Returns:
        -------
        int
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
