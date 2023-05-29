#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """This prints an integer with "{:d}".format().

    A corresponding message is printed to standard error,
    if a ValueError message is caught.

    Args:
        value (int): The integer to print.

    Returns:
        False - If a TypeError or ValueError occurs.
      True - if Otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
