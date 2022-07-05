#!/usr/bin/python3
"""this module changes the string to object"""
import json


def from_json_string(my_str):
    """function that changes json string to json object"""
    return json.loads(my_str)
