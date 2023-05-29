#!/usr/bin/python3


def safe_print_integer(value):
    """This prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
         False - If a TypeError or ValueError occurs.
        True - If Otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
