#!/usr/bin/env python3

import pickle
import os

"""
Module for handling serialization and deserialization of a custom object using `pickle`.

This module defines a `CustomObject` class with attributes for name, age, and whether
the person is a student. It also provides methods for displaying the object's attributes,
and for serializing and deserializing instances of the class, with error handling for
corrupted or inaccessible files.
"""

class CustomObject:
    """
    A class to represent a custom object with attributes: name, age, and is_student.

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
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as pickle_out:
                pickle.dump(self, pickle_out)
            print(f"Object serialized and saved to {filename}")
        except OSError as e:
            print(f"Error saving object to file: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle, with error handling for corrupted or missing files.

        Args:
            filename (str): The name of the file from which the object will be loaded.

        Returns:
            CustomObject: The deserialized object, or None if there was an error.

        Example:
            >>> obj = CustomObject.deserialize('object.pkl')
            >>> if obj:
            >>>     obj.display()
        """
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return None

        try:
            with open(filename, "rb") as pickle_in:
                return pickle.load(pickle_in)
        except (EOFError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object from file: {e}")
            return None
        except OSError as e:
            print(f"Error opening file: {e}")
            return None
