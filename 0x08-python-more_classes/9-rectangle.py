#!/usr/bin/python3
"""This defines a Rectangle class."""


class Rectangle:
    """This represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(personal, width=0, height=0):
        """This initializes a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(personal).number_of_instances += 1
        personal.width = width
        personal.height = height

    @property
    def width(personal):
        """This is the Get/set the width of the Rectangle."""
        return personal.__width

    @width.setter
    def width(personal, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        personal.__width = value

    @property
    def height(personal):
        """This is the Get/set the height of the Rectangle."""
        return personal.__height

    @height.setter
    def height(personal, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        personal.__height = value

    def area(personal):
        """This returns the area of the Rectangle."""
        return (personal.__width * personal.__height)

    def perimeter(self):
        """This returns the perimeter of the Rectangle."""
        if personal.__width == 0 or personal.__height == 0:
            return (0)
        return ((personal.__width * 2) + (personal.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This returns the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("The rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("The rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """This returns a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(personal):
        """This returns the printable representation of the Rectangle.

        It represents the rectangle with the # character.
        """
        if personal.__width == 0 or personal.__height == 0:
            return ("")

        rect = []
        for i in range(personal.__height):
            [rect.append(str(personal.print_symbol)) for j in range(personal.__width)]
            if i != personal.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(personal):
        """This returns the string representation of the Rectangle."""
        rect = "Rectangle(" + str(personal.__width)
        rect += ", " + str(personal.__height) + ")"
        return (rect)

    def __del__(self):
        """This prints a message for every deletion of a Rectangle."""
        type(personal).number_of_instances -= 1
        print("Bye rectangle...")
