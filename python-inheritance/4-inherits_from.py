#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class, but not exactly an
    instance of that class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a
        class that inherited from `a_class`,
        but is not exactly an instance of `a_class`.
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
