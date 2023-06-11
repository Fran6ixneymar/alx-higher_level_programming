#!/usr/bin/python3
"""
This file contains the class BaseGeometry
"""


class BaseGeometry:
    """This is a class with public attribute area"""
    def area(self):
        """This raises an exception when called"""
        raise Exception("area() is not implemented")
