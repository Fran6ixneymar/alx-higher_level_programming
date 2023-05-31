#!/usr/bin/python3
""" This defines a square """


class Square:
    """ A square with private instance attribute size """

    def __init__(self, size=0):
        """
        This initializes the square
        Args:
            size: size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        To finds area of square
        Returns:
            The area of the square
        """

        return self.__size ** 2
