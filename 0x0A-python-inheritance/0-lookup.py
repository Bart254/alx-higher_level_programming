#!/usr/bin/python3
"""Module looks up all the attributes of an object
"""


def lookup(obj):
    """ Returns all the attributes of an object as a list
    """
    if type(obj) is not None:
        return list(dir(obj))
