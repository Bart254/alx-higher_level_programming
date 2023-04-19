#!/usr/bin/python3
""" add_integer module"""


def add_integer(a, b):
    """ returns the sum of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("{} must be an integer".format(a))
    if not isinstance(b, (int, float)):
        raise TypeError("{} must be an integer".format(b))
    return int(a) + int(b)
