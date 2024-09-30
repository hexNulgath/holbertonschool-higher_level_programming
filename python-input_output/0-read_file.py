#!/usr/bin/python3
"""
This module provides a simple function to read
and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads and prints the content of a specified file.

    Args:
        filename (str): The name of the file to be read. If not provided,
                        an empty string is used,
                        which will raise a FileNotFoundError.

    Returns:
        None: The function prints each line of the file as it reads it.

    Raises:
        FileNotFoundError: If the file specified by `filename` does not exist.
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
