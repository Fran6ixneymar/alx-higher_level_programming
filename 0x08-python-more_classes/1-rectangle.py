#!/usr/bin/python3
"""
This defines a class Rectangle
"""


class Rectangle:
    """This is a representation of a rectangle"""
    def __init__(personal, width=0, height=0):
        """This initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(personal):
        """This is a getter for the private instance attribute width"""
        return personal.__width

    @width.setter
    def width(personal, value):
        """This is a setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        personal.__width = value

    @property
    def height(personal):
        """This is a getter for the private instance attribute height"""
        return personal.__height

    @height.setter
    def height(personal, value):
        """This is a setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        personal.__height = value
