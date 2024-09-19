#!/usr/bin/python3
"""
This module defines a `Rectangle` class that models a rectangle
with attributes such as width and height. It provides methods
for calculating area, perimeter, and printing a visual representation
of the rectangle.

Classes:
    - Rectangle: A class for creating and managing rectangles,
    including methods for area, perimeter, and comparisons of rectangles.
"""


class Rectangle:
    """
    A class to represent a Rectangle.

    Class Attributes
    ----------------
    number_of_instances : int
        Tracks the number of instances of the Rectangle class.
    print_symbol : str
        The symbol used to visually represent the rectangle (default is '#').

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).

    Methods
    -------
    __init__(self, width=0, height=0):
        Initializes the rectangle with the given width and height.

    area(self) -> int:
        Returns the area of the rectangle.

    perimeter(self) -> int:
        Returns the perimeter of the rectangle,
        or 0 if either width or height is 0.

    __str__(self) -> str:
        Returns a string representation of the rectangle for visual printing.

    print(self):
        Prints the rectangle using the specified print_symbol.

    __repr__(self) -> str:
        Returns a string representation of the rectangle
        in the format "Rectangle(width, height)".

    __del__(self):
        Prints a message when the rectangle is
        deleted and decrements the instance count.

    bigger_or_equal(rect_1, rect_2):
        Static method that returns the rectangle
        with the greater or equal area.
        Raises a TypeError if the arguments are not Rectangle instances.

    square(cls, size=0):
        Class method that returns a new Rectangle
        instance with width and height equal to size.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with the given width and height.
        Increments the instance counter.

        Parameters:
        -----------
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        -----------
        value (int): The new width value. Must be a non-negative integer.

        Raises:
        -------
        TypeError: If width is not an integer.
        ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
        -----------
        value (int): The new height value. Must be a non-negative integer.

        Raises:
        -------
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
        Returns the area of the rectangle.

        Returns:
        --------
        int: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
        --------
        int: The perimeter of the rectangle (2 * (width + height)).
             Returns 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Provides a string representation of the rectangle
        using the `print_symbol` for visual representation.

        Returns:
        --------
        str: A visual representation of the
        rectangle made up of `print_symbol`.
        """
        if self.height == 0 or self.width == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.width for row in range(self.height))

    def print(self):
        """
        Prints the rectangle using the `print_symbol`.
        If the width or height is 0, it prints an empty line.
        """
        print(self.__str__())

    def __repr__(self):
        """
        Returns a string representation of the rectangle instance.

        Returns:
        --------
        str: A string in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when a rectangle instance is deleted
        and decrements the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles by their area and
        returns the larger or equal rectangle.

        Parameters:
        -----------
        rect_1 : Rectangle
            The first rectangle to compare.
        rect_2 : Rectangle
            The second rectangle to compare.

        Returns:
        --------
        Rectangle: The rectangle with the larger or equal area.

        Raises:
        -------
        TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new rectangle instance with
        equal width and height (a square).

        Parameters:
        -----------
        size : int
            The size of the sides of the square (default is 0).

        Returns:
        --------
        Rectangle: A new instance of a square-shaped rectangle.
        """
        return cls(size, size)
