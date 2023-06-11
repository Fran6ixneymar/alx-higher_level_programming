#!/usr/bin/python3
"""
This file contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a representation of a rectangle"""
    def __init__(personal, width, height):
        """This is the instantiation of the rectangle"""
        personal.integer_validator("width", width)
        personal.__width = width
        personal.integer_validator("height", height)
        personal.__height = height
