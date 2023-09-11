#!/usr/bin/python3
"""Checks if an object is a subclass of a class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is a subclass"""
    if obj is not None and a_class is not None:
        if issubclass(obj, a_class):
            return True
    return False
