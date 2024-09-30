#!/usr/bin/python3

"""
This module defines a Student class with attributes for first name,
last name, and age. It also includes a method to retrieve the
instance's attributes in dictionary format, suitable for JSON encoding.
"""


class Student:
    """
    A class used to represent a Student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is provided, only the attributes listed in attrs
        are included in the dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include.
                                    If None, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {item: self.__dict__[item]
                    for item in attrs
                    if item in self.__dict__}

        else:
            return self.__dict__
