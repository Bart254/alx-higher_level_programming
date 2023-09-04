#!/usr/bin/python3
""" Module containing a function for addition
"""


def add_integer(a, b=98):
    """ Adds a and b then returns the sum
    """
    type_a = 1 if isinstance(a, int) else (2 if isinstance(a, float) else 0)
    type_b = 1 if isinstance(b, int) else (2 if isinstance(b, float) else 0)

    if type_a == 0:
        raise TypeError("a must be an integer")
    if type_b == 0:
        raise TypeError("b must be an integer")
    if type_a == 2:
        a = int(a)
    if type_b == 2:
        b = int(b)
    return a+b
