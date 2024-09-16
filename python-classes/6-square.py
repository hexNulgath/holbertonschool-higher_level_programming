#!/usr/bin/python3
class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square, which represents the length of each side (default is 0).
    position : tuple
        The position of the square, which represents the offset when printing the square (default is (0, 0)).

    Methods
    -------
    area():
        Returns the area of the square.
    
    my_print():
        Prints the square using the '#' character with spaces based on the position.

    Properties
    ----------
    size : int
        Gets or sets the size of the square, with a validation check.
    position : tuple
        Gets or sets the position of the square, with a validation check.
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(position, tuple) and len(position) == 2 and all(isinstance(item, int) for item in position) and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else: 
            raise TypeError("size must be an integer")

    def area(self):
      return self.__size**2
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for  i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else: 
            raise TypeError("size must be an integer")
        
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(item, int) for item in value) and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
