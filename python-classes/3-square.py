#!/usr/bin/python3
class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square, which represents the length of each side (default is 0).

    Methods
    -------
    area():
        Returns the area of the square.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else: 
            raise TypeError("size must be an integer")

    def area(self):
      return self.__size**2
