#!/usr/bin/python3
"""
This file contains the json str function
"""

import json


def from_json_string(my_str):
    """This returns an object represented by a JSON string"""
    return json.loads(my_str)
