#!/usr/bin/python3
"""Rectangle Module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle, a subclass of BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes a rectangle object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Returns informal presentation of the Rectangle object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
