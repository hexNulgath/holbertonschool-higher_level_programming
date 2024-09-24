#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module: base_geometry

This module defines a base class for geometric shapes and a subclass
for rectangular shapes.

Classes:
    - Rectangle: A class representing a rectangle, subclass of BaseGeometry.
"""

class Rectangle(BaseGeometry):
    """
    A rectangle shape that inherits from BaseGeometry.

    This class defines a rectangle by its width and height, ensuring
    that both are validated as positive integers during initialization.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates that both width and height are positive integers using
        the integer_validator method inherited from BaseGeometry.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
