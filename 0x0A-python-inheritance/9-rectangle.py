#!/usr/bin/python3
"""
This file contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """This is a class with public instance methods area and integer_validator"""
    def area(personal):
        """It raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(personal, name, value):
        """This validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a representation of a rectangle"""
    def __init__(personal, width, height):
        """This is the instantiation of the rectangle"""
        personal.integer_validator("width", width)
        personal.__width = width
        personal.integer_validator("height", height)
        personal.__height = height

    def area(personal):
        """returns the area of the rectangle"""
        return personal.__width * personal.__height

    def __str__(personal):
        """This is an informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(personal.__width, personal.__height)
