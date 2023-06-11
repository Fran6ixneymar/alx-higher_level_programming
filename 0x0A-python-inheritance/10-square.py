#!/usr/bin/python3
"""
This file contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a representation of a square"""
    def __init__(personal, size):
        """This is the instantiation of the square"""
        personal.integer_validator("size", size)
        personal.__size = size
        super().__init__(size, size)

    def area(personal):
        """"returns the area of the square"""
        return personal.__size ** 2
