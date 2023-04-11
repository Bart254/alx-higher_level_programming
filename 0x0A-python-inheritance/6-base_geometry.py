#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry  class
    Attributes:
            area(method)
    """
    def area(self):
        """raises an exception with message area() is not implemented"""
        raise Exception("area() is not implemented")
