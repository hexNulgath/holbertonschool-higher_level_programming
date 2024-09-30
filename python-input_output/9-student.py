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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the instance's attributes.
                  The keys are 'first_name', 'last_name', and 'age'.

        Example:
            student = Student("John", "Doe", 22)
            student_dict = student.to_json()
            # Result: {'first_name': 'John', 'last_name': 'Doe', 'age': 22}
        """
        return self.__dict__
