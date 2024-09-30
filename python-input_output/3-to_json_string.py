#!/usr/bin/python3
import json

"""
This module provides a function to convert a Python object to a JSON string.
"""


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj (Any): The Python object to be serialized to JSON.

    Returns:
        str: The JSON-formatted string representation of `my_obj`.

    Raises:
        TypeError: If the object is not serializable to JSON.
    """
    return json.dumps(my_obj)
