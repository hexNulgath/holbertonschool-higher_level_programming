#!/usr/bin/python3
class BaseGeometry:
    """
    A base class for geometric shapes.

    This class serves as a foundation for defining various geometric shapes,
    providing methods for validating integer values and calculating the area.
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

    This class defines a rectangle by its width and height, ensuring that
    both are validated as positive integers during initialization.
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

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.

        The output format is: [Rectangle] width/height.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[{self.__class__}] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle calculated as width * height.
        """
        return self.__width * self.__height


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
        method inherited from BaseGeometry.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to zero.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        The output format is: [Square] size/size.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
