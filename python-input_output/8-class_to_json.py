#!/usr/bin/python3

"""
This module provides a function to serialize an object's attributes
into a JSON-formatted string.
"""
import json


def class_to_json(obj):
    """
    Serializes an object's instance variables (attributes) into a
    JSON-formatted string.

    Args:
        obj (Any): The object to be serialized.

    Returns:
        str: A JSON string representation of the object's attributes.

    Example:
        class MyClass:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        obj = MyClass("Alice", 30)
        json_string = class_to_json(obj)
        # Result: '{"name": "Alice", "age": 30}'
    """
    return json.dumps(obj.__dict__)
