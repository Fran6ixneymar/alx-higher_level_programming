#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """This represents a Square, inheriting from Rectangle."""

    def __init__(personal, size, x=0, y=0, id=None):
        """This initializes a new Square.

        Args:
            size (int): The size of the Square.
            x (int): The x-coordinate of the Square's position.
            y (int): The y-coordinate of the Square's position.
            id (int): The identity of the Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(personal):
        """This sets the size of the Square.

        Returns:
            int: The size of the Square.
        """
        return personal.width

    @size.setter
    def size(personal, value):
        """This sets the size of the Square.

        Args:
            value (int): The size value to set.
        """
        personal.width = value
        personal.height = value

    def __str__(personal):
        """This returns a string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            personal.id, personal.x, personal.y, personal.width
        )

    def update(personal, *args, **kwargs):
        """This updates the attributes of the Square.

        Args:
            *args: List of arguments.
            **kwargs: Dictionary of keyword arguments.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(personal, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(personal, key, value)
    def to_dictionary(personal):
        """This returns the dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square.
        """
        return {
            "id": personal.id,
            "size": personal.size,
            "x": personal.x,
            "y": personal.y,
        }
