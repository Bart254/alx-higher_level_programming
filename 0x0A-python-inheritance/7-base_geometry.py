#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry  class
    Methods:
        area(public instance): raises an exception with error message
        integer_validator(public instance): validates an integer
    """

    def area(self):
        """raises an exception with message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if arg value is of int type and greater than 0
            and displays an error message otherwise
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
