#!/usr/bin/python3

"""
This module provides a function to load a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a file containing JSON data.

    Args:
        filename (str): The name of the file to load the JSON data from.

    Returns:
        Any: The Python object resulting from the deserialization of the
             JSON data in the file.

    Raises:
        json.JSONDecodeError: If the file content is not valid JSON.
        FileNotFoundError: If the file does not exist.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
