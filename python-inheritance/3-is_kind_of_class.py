#!/usr/bin/python3
"""
Module: is_kind_of_class
This module defines a function that checks whether an object is an instance of,
or an instance of a subclass of, a specified class.

The function is useful for verifying if an object is either a direct instance
of a class or belongs to a subclass of the given class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or an instance of a subclass of,
    a specified class.

    This function uses isinstance() to determine if the object is an instance
    of the specified class or one of its subclasses.

    Args:
        obj: The object to check.
        a_class: The class (or parent class) to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or a
              subclass of it. False otherwise.

    Example:
        >>> is_kind_of_class(5, int)
        True
        >>> is_kind_of_class(True, int)
        True
        >>> is_kind_of_class("hello", int)
        False
        >>> is_kind_of_class(5.0, float)
        True
    """
    return isinstance(obj, a_class)
