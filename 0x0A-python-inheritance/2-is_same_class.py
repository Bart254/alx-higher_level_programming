#!/usr/bin/python3
"""Compares an object to a class
"""


def is_same_class(obj, a_class):
    """Returns true if object is an instance of a_class
    Otherwise returns false"""
    if obj is not None and a_class is not None:
        if isinstance(obj, a_class):
            return True
    return False
