#!/usr/bin/python3
"""A Rectangle Module
"""


class Rectangle:
    """A class storing attributes and methods of a rectangle
        Attributes:
            width(int): private instance attr with property
            height(int): private instace attr with property
    """
    def __init__(self, width=0, height=0):
        """initializes private instace width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width to args value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
