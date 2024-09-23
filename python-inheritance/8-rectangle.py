#!/usr/bin/python3
"""
Module: base_geometry

This module defines a base class for geometric shapes. It is designed as a
foundation upon which more complex geometric classes and functionality can
be built.

Classes:
    - BaseGeometry: An empty base class for geometry objects.
"""


class BaseGeometry:
    """
    A base class for geometry objects.

    This class serves as a foundation for defining geometric shapes.
    It includes methods for validating integer values and
    calculating the area.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.

        This method is intended to be overridden by subclasses that define
        specific geometric shapes. Each subclass should implement the area()
        method to compute the area of the shape it represents.

        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer greater than zero.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if value.__class__ is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
