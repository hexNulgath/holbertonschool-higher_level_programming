#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        A list of strings representing the names of attributes and methods
        available in the given object. This includes both instance-specific
        and inherited attributes/methods.
    """
    return dir(obj)
