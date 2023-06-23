#!/usr/bin/python2

from models.base import Base


class Rectangle(Base):
    """This represents a Rectangle."""

    def __init__(personal, width, height, x=0, y=0, id=None):
        """This initializes a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x-coordinate of the Rectangle's position.
            y (int): The y-coordinate of the Rectangle's position.
            id (int): The identity of the Rectangle.
        """
        super().__init__(id)
        personal.width = width
        personal.height = height
        personal.x = x
        personal.y = y

    @property
    def width(personal):
        """This gets the width of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return personal.__width

    @width.setter
    def width(personal, value):
        """This sets the width of the Rectangle.

        Args:
            value (int): The width value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        personal.__width = value

    @property
    def height(personal):
        """This gets the height of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return personal.__height

    @height.setter
    def height(personal, value):
        """This sets the height of the Rectangle.

        Args:
            value (int): The height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        personal.__height = value

    @property
    def x(personal):
        """This sets the x-coordinate of the Rectangle's position.

        Returns:
            int: The x-coordinate of the Rectangle's position.
        """
        return personal.__x

    @x.setter
    def x(personal, value):
        """This sets the x-coordinate of the Rectangle's position.

        Args:
            value (int): The x-coordinate value to set.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        personal.__x = value

    @property
    def y(personal):
        """This sets the y-coordinate of the Rectangle's position.

        Returns:
            int: The y-coordinate of the Rectangle's position.
        """
        return personal.__y

    @y.setter
    def y(personal, value):
        """This sets the y-coordinate of the Rectangle's position.

        Args:
            value (int): The y-coordinate value to set.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        personal.__y = value

    def area(personal):
        """This calculates the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return personal.width * personal.height

    def display(personal):
        """This displays the Rectangle instance using '#' characters."""
        for _ in range(personal.y):
            print()
        for _ in range(personal.height):
            print(" " * personal.x + "#" * personal.width)

    def __str__(personal):
        """This returns a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            personal.id, personal.x, personal.y, personal.width, personal.height
        )

    def update(personal, *args, **kwargs):
        """This assigns key/value arguments to attributes."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(personal, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(personal, key, value)

    def to_dictionary(personal):
        """This returns the dictionary representation of the Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle.
        """
        return {
            "id": personal.id,
            "width": personal.width,
            "height": personal.height,
            "x": personal.x,
            "y": personal.y,
        }
