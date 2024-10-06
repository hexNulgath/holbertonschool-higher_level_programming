#!/usr/bin/env python3

import pickle

"""
Module for handling serialization and deserialization
of a custom object using `pickle`.

This module defines a `CustomObject` class
with attributes for name, age, and whether
the person is a student. It also provides
methods for displaying the object's attributes,
and for serializing and deserializing instances of the class.

Classes:
    - CustomObject: A class representing a custom
    object with methods to serialize and deserialize it.
"""


class CustomObject:
    """
    A class to represent a custom object with
    attributes: name, age, and is_student.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student or not.

    Methods:
        display(): Prints the object's attributes to the console.
        serialize(filename): Serializes the object to a file.
        deserialize(filename): Deserializes the object from a file.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and is_student status.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes to the console in a formatted string.

        Example:
            >>> obj = CustomObject("Alice", 25, True)
            >>> obj.display()
            Name: Alice
            Age: 25
            Is Student: True
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Args:
            filename (str): The name of the
            file where the object will be saved.

        Raises:
            IOError: If there is an error writing to the file.

        Example:
            >>> obj = CustomObject("Alice", 25, True)
            >>> obj.serialize('object.pkl')
        """
        with open(filename, "wb") as pickle_out:
            pickle.dump(self, pickle_out)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): The name of the file
            from which the object will be loaded.

        Returns:
            CustomObject: The deserialized object.

        Raises:
            IOError: If there is an error reading from the file.
            pickle.UnpicklingError: If the file contains invalid pickle data.

        Example:
            >>> obj = CustomObject.deserialize('object.pkl')
            >>> obj.display()
        """
        with open(filename, "rb") as pickle_in:
            return pickle.load(pickle_in)
