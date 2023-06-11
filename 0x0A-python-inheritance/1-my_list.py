#!/usr/bin/python3
"""
This code contains the MyList class
"""


class MyList(list):
    """This is a subclass of list"""
    def __init__(self):
        """It initializes the object"""
        super().__init__()

    def print_sorted(self):
        """And prints the sorted list"""
        print(sorted(self))
