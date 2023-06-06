#!/usr/bin/python3
# 101-locked_class.py

"""This file defines a locked class."""


class LockedClass:
    """
    It prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
