#!/usr/bin/python3
"""
Module: inherits_from
This module defines a function that checks whether an object is an instance
of a class that inherited (directly or indirectly) from a specified class,
but is not exactly an instance of the specified class.

The function is useful for determining whether an object belongs to a subclass
of a given class, without being an exact instance of that class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly)
    from the specified class, but is not exactly an instance of that class.

    This function returns True if the object is an instance of a
    subclass of the specified class but not an instance of the class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited from
              `a_class`, but is not exactly an instance of `a_class`.
              False otherwise.

    Example:
        >>> class A: pass
        >>> class B(A): pass
        >>> obj = B()
        >>> inherits_from(obj, A)
        True
        >>> inherits_from(obj, B)
        False
        >>> inherits_from(obj, object)
        True
    """
    return isinstance(obj, a_class) and obj.__class__ is not a_class
