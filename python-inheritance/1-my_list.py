#!/usr/bin/python3
"""
Module: my_list
This module defines a custom list class that inherits from the built-in list
and provides additional functionality to print a sorted version of the list.
"""


class MyList(list):
    """
    A subclass of the built-in list class that adds a method to print the list
    in a sorted order.

    Methods:
        print_sorted(self):
            Prints the elements of the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.

        The method does not modify the original list;
        it prints a sorted version of it.
        """
        print(sorted(self))
