#!/usr/bin/python3
"""
Module: is_same_class
This module defines a function that checks whether an object is exactly
an instance of a specified class.

The function is useful for determining if an object is an instance of the
specified class, but it will return False if the object is an instance of
a subclass of the given class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    This function compares the class of the object with the specified class.
    It returns True only if the object is exactly an instance of the specified
    class, not a subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool:
        True if the object is exactly an instance of the specified class,
        False if the object is an instance of a subclass or a different class.

    Example:
        >>> is_same_class(5, int)
        True
        >>> is_same_class(True, int)
        False
        >>> is_same_class("hello", str)
        True
        >>> is_same_class(5.0, int)
        False
    """
    return obj.__class__ is a_class
