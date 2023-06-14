#!/usr/bin/python3
"""
This is a function that appends a string
"""


def append_write(filename="", text=""):
    """This returns the number of added characters:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
