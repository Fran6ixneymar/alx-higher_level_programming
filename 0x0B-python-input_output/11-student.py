#!/usr/bin/python3
"""
This file contains the clas "Student"
"""


class Student:
    """This representation of a student"""
    def __init__(personal, first_name, last_name, age):
        """This initializes the student"""
        personal.first_name = first_name
        personal.last_name = last_name
        personal.age = age

    def to_json(personal, attrs=None):
        """This returns a dictionary representation of a Student instance
        with specified attributes"""
        if attrs is None:
            return personal.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = personal.__dict__[a]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(personal, json):
        """This replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(personal, key, json[key])
            except FileNotFoundError:
                pass
