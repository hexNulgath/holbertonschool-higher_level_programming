#!/usr/bin/python3

"""
This module provides a function to convert an object's attributes
to a dictionary, making it suitable for JSON encoding.
"""


def class_to_json(obj):
    """
    Converts an object's instance variables (attributes) into a dictionary
    format suitable for JSON serialization.

    Args:
        obj (Any): The object whose attributes are to be converted.

    Returns:
        dict: A dictionary containing the object's instance variables.

    Example:
        class MyClass:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        obj = MyClass("Alice", 30)
        obj_dict = class_to_json(obj)
        # Result: {'name': 'Alice', 'age': 30}
    """
    return obj.__dict__
