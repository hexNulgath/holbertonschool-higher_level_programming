#!/usr/bin/python3

"""
This module provides a function to save a Python object as a JSON string
to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON format.

    Args:
        my_obj (Any): The Python object to serialize and save.
        filename (str): The name of the file where the JSON string will be
                        written.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
