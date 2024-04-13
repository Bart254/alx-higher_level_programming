#!/usr/bin/python3
""" Max Integer
"""


def max_integer(list=[]):
    """ Returns the maximum integer in a list

    Parameters
    ----------
    list: list
        A list of integers

    Returns
    ------
    Max integer in the list passed
    """
    if not list or len(list) == 0:
        return None
    _max = list[0]
    i = 1
    while i < len(list):
        if list[i] > _max:
            _max = list[i]
        i += 1
    return _max
