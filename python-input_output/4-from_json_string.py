#!/usr/bin/python3

"""
This module provides a function to deserialize a JSON string
into a Python object.
"""
import json


def from_json_string(my_str):
    """
    Deserializes a JSON-formatted string into a Python object.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        Any: The Python object resulting from the deserialization of the
             JSON string.

    Raises:
        json.JSONDecodeError: If the string is not a valid JSON.
    """
    return json.loads(my_str)
