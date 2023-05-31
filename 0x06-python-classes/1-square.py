#!/usr/bin/python3
"""This is the definition of a square class"""


class Square:
    """This represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """This Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: Nothing
        """
        self.__size = size
