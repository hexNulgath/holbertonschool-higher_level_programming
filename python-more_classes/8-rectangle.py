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
    A class used to represent a Rectangle.

    Class Attributes
    ----------------
    number_of_instances : int
        Tracks the number of Rectangle instances.

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).

    Methods
    -------
    __init__(self, width=0, height=0):
        Initializes the rectangle object with width and height.

    width(self):
        Gets the width of the rectangle.

    width(self, value):
        Sets the width of the rectangle.
        Ensures the value is a non-negative integer.

    height(self):
        Gets the height of the rectangle.

    height(self, value):
        Sets the height of the rectangle.
        Ensures the value is a non-negative integer.

    area(self):
        Returns the area of the rectangle.

    perimeter(self):
        Returns the perimeter of the rectangle.
        Returns 0 if either width or height is 0.

    __str__(self):
        Returns a string representation of the rectangle
        using the `#` character.

    print(self):
        Prints the rectangle using the `#` character.
        If width or height is 0, prints an empty line.

    __repr__(self):
        Returns a string that represents the rectangle
        in the format "Rectangle(width, height)".

    __del__(self):
        Prints a message when a rectangle instance is deleted.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with given width and height.
        Increments the instance counter upon creation.

        Parameters:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        value (int): The new width value. Must be a non-negative integer.

        Raises:
        TypeError: If width is not an integer.
        ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        value (int): The new height value. Must be a non-negative integer.

        Raises:
        TypeError: If height is not an integer.
        ValueError: If height is negative.
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
        int: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle (2 * (width + height)),
             or 0 if either the width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Provides a string representation of the
        rectangle using the `#` character.

        Returns:
        str: A visual representation of the rectangle
        made up of `#` characters.
        """
        if self.height == 0 or self.width == 0:
            return ""
        symbol = self._get_print_symbol()
        return "\n".join(symbol * self.width for row in range(self.height))

    def print(self):
        """
        Prints the rectangle using the `#` character.
        If width or height is 0, it prints an empty line.
        """
        if self.height == 0 or self.width == 0:
            print()
        else:
            symbol = self._get_print_symbol()
            for row in range(self.height):
                print(symbol * self.width)

    def __repr__(self):
        """
        Provides a string representation of the rectangle instance.

        Returns:
        str: A string that represents the rectangle in
        the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when a rectangle instance is
        deleted and decrements the instance count.
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    def _get_print_symbol(self):
        """
        Converts the `print_symbol` into a string.
        If `print_symbol` is a list, it keeps it as is for printing.
        """
        if isinstance(self.print_symbol, list):
            return str(self.print_symbol)
        return str(self.print_symbol)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            a = rect_1.area()
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle):
            b = rect_2.area()
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if a >= b:
            return rect_1
        else:
            return rect_2
