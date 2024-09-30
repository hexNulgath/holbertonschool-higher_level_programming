#!/usr/bin/python3
"""
This module provides a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoding) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file where the text will be written.
                        If not provided, an empty string will cause an error.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If there is an issue writing to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
