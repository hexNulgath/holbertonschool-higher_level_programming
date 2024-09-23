#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or an instance of a subclass of,
    a specified class.

    Args:
        obj: The object to check.
        a_class: The class (or parent class) to compare against.

    Returns:
        True if the object is an instance of the specified
        class or a subclass of it. False otherwise.

    Example:
        >>> is_kind_of_class(5, int)
        True
        >>> is_kind_of_class(True, int)
        True
        >>> is_kind_of_class("hello", int)
        False
    """
    return isinstance(obj, a_class)
