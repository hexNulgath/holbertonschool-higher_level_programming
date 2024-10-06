#!/usr/bin/env python3

"""
Module for serializing and deserializing
Python data structures to/from JSON files.

This module provides simple functions for
saving Python data structures (like dictionaries,
lists, etc.) to JSON files and reading them
back. It uses the `json` module for handling
the serialization and deserialization of data.

Functions:
    - serialize_and_save_to_file: Serializes Python data to a JSON file.
    - load_and_deserialize: Deserializes Python data from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize Python data (e.g., dict, list) and save it to a JSON file.

    Args:
        data: The Python data structure to be
        serialized (e.g., dict, list, etc.).
        filename (str): The name of the JSON
        file where the data will be stored.

    Raises:
        TypeError: If the data is not serializable to JSON.
        IOError: If there is an issue writing to the file.

    Example:
        >>> data_to_save = {'name': 'Alice', 'age': 30}
        >>> serialize_and_save_to_file(data_to_save, 'data.json')
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize Python data from a JSON file.

    Args:
        filename (str): The name of the JSON file from which to load the data.

    Returns:
        The deserialized Python data structure.

    Raises:
        json.JSONDecodeError: If the file content is not valid JSON.
        IOError: If there is an issue reading from the file.

    Example:
        >>> loaded_data = load_and_deserialize('data.json')
        >>> print(loaded_data)  # Output: {'name': 'Alice', 'age': 30}
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
