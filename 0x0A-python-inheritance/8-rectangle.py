#!/usr/bin/python3
"""Creates a Rectangle class, a subclas of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """My Rectangle Class"""
    def __init__(self, width, height):
        """initializes a rectangle with private attr width and height"""
        self.integer_validator("width", width)
        self.integr_validator("height", height)
        self.__width = width
        self.__height = height
