#!/usr/bin/python3
"""
This defines a class Rectangle
"""


class Rectangle:
    """This is the representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(personal, width=0, height=0):
        """This initializes the rectangle"""
        personal.width = width
        personal.height = height
        Rectangle.number_of_instances += 1

    def __del__(personal):
        """It prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(personal):
        """This is the getter for the private instance attribute width"""
        return personal.__width

    @width.setter
    def width(personal, value):
        """This is the setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        personal.__width = value

    @property
    def height(personal):
        """This is the getter for the private instance attribute height"""
        return personal.__height

    @height.setter
    def height(personal, value):
        """This is the setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        personal.__height = value

    def area(personal):
        """This returns the area of the rectangle"""
        return personal.__width * personal.__height

    def perimeter(personal):
        """This returns the perimeter of the rectangle"""
        if personal.__width == 0 or personal.__height == 0:
            return 0
        return (personal.__width * 2) + (personal.__height * 2)

    def __str__(personal):
        """This returns printable string representation of the rectangle"""
        string = ""
        if personal.__width != 0 and personal.__height != 0:
            string += "\n".join(str(personal.print_symbol) * personal.__width
                                for j in range(personal.__height))
        return string

    def __repr__(personal):
        """This returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(personal.__width, personal.__height)
