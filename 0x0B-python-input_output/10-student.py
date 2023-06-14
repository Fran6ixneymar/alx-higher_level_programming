#!/usr/bin/python3
"""This defines a class Student."""


class Student:
    """This represents a student."""

    def __init__(personal, first_name, last_name, age):
        """It initializes a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        personal.first_name = first_name
        personal.last_name = last_name
        personal.age = age

    def to_json(personal, attrs=None):
        """This gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(personal, k) for k in attrs if hasattr(personal, k)}
        return personal.__dict__
