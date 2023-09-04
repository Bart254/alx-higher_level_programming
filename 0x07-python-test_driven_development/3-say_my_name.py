#!/usr/bin/python3
""" Module for printing out name
"""


def say_my_name(first_name, last_name=""):
    """ Returns the last name and first name in a sentence
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
