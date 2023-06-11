#!/usr/bin/python3
"""
This file contains the class MyInt
"""


class MyInt(int):
    """This is the rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """It creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(personal, other):
        """what was != is now =="""
        return int(personal) != other

    def __ne__(personal, other):
        """what was == is now !="""
        return int(personal) == other
