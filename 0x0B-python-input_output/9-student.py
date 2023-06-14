#!/usr/bin/python3
"""
This file contains the class "Student"
"""


class Student:
    """This is the representation of a student"""
    def __init__(personal, first_name, last_name, age):
        """This initializes the student"""
        personal.first_name = first_name
        personal.last_name = last_name
        personal.age = age

    def to_json(personal):
        """This returns a dictionary representation of a Student instance"""
        return personal.__dict__
