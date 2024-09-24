#!/usr/bin/python3
"""
Module: base_geometry

This module defines a base class for geometric shapes and its subclasses.
The module includes a base class `BaseGeometry` that provides methods for
geometry-related functionality, such as validating integers and calculating
area, along with specific shapes such as `Rectangle` and `Square`.

Classes:
    - Square: A subclass of Rectangle that defines a square shape.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square shape that inherits from Rectangle.

    This class defines a square by its size, using the width and height
    of the rectangle to be the same value.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (width and height).

        Validates that size is a positive integer using the integer_validator
        method inherited from BaseGeometry. Then calls the Rectangle's
        initializer with the same value for both width and height.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to zero.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

