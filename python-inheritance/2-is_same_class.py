#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class.
        False if the object is an instance of a subclass or a different class.

    Example:
        >>> is_same_class(5, int)
        True
        >>> is_same_class(True, int)
        False
    """
    return obj.__class__ is a_class
