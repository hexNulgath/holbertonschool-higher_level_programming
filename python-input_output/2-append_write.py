#!/usr/bin/python3
"""
This module provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF-8 encoding) and returns the number
    of characters written.

    Args:
        filename (str): The name of the file where the text will be appended.
                        If not provided, an empty string may cause an error.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If there is an issue appending to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
