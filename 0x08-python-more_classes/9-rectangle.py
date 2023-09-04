#!/usr/bin/python3
"""A Rectangle Module
"""


class Rectangle:
    """A class storing attributes and methods of a rectangle
        Attributes:
            width(int): private instance attr with property
            height(int): private instace attr with property
            number_of_instances: records number of objects made
            print_symbol: the symbol to be used for the rectangle
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
        self.add_instance()

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

    def area(self):
        """ returns the area of rectangle (width * height)"""
        return self.width * self.height

    def perimeter(self):
        """ returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ sting repr of rectangle
        Prints # in the shape of rectangle's width and height
        """
        if self.width == 0 or self.height == 0:
            return ""
        a = self.print_symbol
        if not isinstance(a, str):
            a = str(a)
        return (a * self.width + "\n") * (self.height - 1) + a * self.width

    def __repr__(self):
        """ official representation of rectangle object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """deletes an instance of rectangle"""
        print("Bye rectangle...")
        self.del_instance()

    @classmethod
    def add_instance(cls):
        cls.number_of_instances += 1

    @classmethod
    def del_instance(cls):
        cls.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
