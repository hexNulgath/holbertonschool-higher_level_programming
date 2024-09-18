#!/usr/bin/python3
"""
This module defines a Rectangle class that handles the creation
and manipulation of rectangle objects.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
    ----------
    __width : int
        The width of the rectangle (private).
    __height : int
        The height of the rectangle (private).

    Methods:
    -------
    __init__(self, width=0, height=0):
        Initializes the rectangle with width and height.

    width(self):
        Getter for the width attribute.

    width(self, value):
        Setter for the width attribute. Checks for type and value errors.

    height(self):
        Getter for the height attribute.

    height(self, value):
        Setter for the height attribute. Checks for type and value errors.
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
        ValueError:
            If width or height is negative.
        TypeError:
            If width or height is not an integer.
        """
        if isinstance(width, int) and width >= 0:
            __width = width
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if isinstance(height, int) and width >= 0:
            __height = height
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
        -------
        int
            The width of the rectangle.
        """
        return self.__width

    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
        -------
        int
            The height of the rectangle.
        """
        return self.__height

    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        ----------
        value : int
            The new width of the rectangle.

        Raises:
        ------
        ValueError:
            If width is negative.
        TypeError:
            If width is not an integer.
        """
        if isinstance(value, int) and value >= 0:
            self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
        ----------
        value : int
            The new height of the rectangle.

        Raises:
        ------
        ValueError:
            If height is negative.
        TypeError:
            If height is not an integer.
        """
        if isinstance(value, int) and value >= 0:
            self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
