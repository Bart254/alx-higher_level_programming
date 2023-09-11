#!/usr/bin/python3
"""Checks if an object is instance of or a subclass of a class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is instance of a_class
    or if it is a subclass"""
    if obj is not None and a_class is not None:
        if isinstance(obj, a_class) or if issubclass(obj, a_class):
            return True
    return False
