#!/usr/bin/python3
"""Module that creates a rectangle class"""


class Rectangle:
    """A class storing attributes and methods of a rectangle
        Attributes:
            width(int): private instance attr with property
            height(int): private instace attr with property
            number_of_instances: records number of objects made
            print_symbol(any type): public class symbol used to print rectangle
        Methods:
            area: public instance, returns area
            perimeter: public instance, returns perimeter
            __del__: displays a messge before deleting an object
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes private instace width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width to args value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle (width * height)"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ sting repr of rectangle
        Prints # in the shape of rectangle's width and height
        """
        return (Rectangle.print_symbol * self.__width + "\n") * self.__height

    def __repr__(self):
        """ official representation of rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
