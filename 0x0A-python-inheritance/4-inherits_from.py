#!/usr/bin/ython3
"""checks is an object is a subclass of a_class"""


def inherits_from(obj, a_class):
    """Returns True or False"""
    return True if issubclass(obj, a_class) else False
