#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    This function retrieves the names of all the attributes and methods
    of a given object, including both instance-specific and inherited
    attributes/methods. This can be useful for introspection or debugging.

    Args:
        obj: The object whose attributes and methods are to be listed.
             This can be any Python object, including instances of classes.

    Returns:
        list: A list of strings representing the names of attributes
              and methods available in the given object.

    Example:
        >>> class MyClass:
        ...     def my_method(self):
        ...         pass
        ...
        >>> obj = MyClass()
        >>> lookup(obj)
        ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
         '__format__', '__ge__', '__getattribute__', '__getitem__',
         '__gt__', '__init__', '__init_subclass__', '__le__', '__lt__',
         '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
         '__repr__', '__setattr__', '__sizeof__', '__str__',
         '__subclasshook__', 'my_method']
    """
    return dir(obj)
