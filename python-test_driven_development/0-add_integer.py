#!/usr/bin/python3
"""
This module provides a function 'add_integer' that adds two integers.

Args:
    a: must be an integer or a value convertible to an integer.
    b: must be an integer or a value convertible to an integer (default is 98).
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or cannot be cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
