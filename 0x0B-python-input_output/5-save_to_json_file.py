#!/usr/bin/python3
"""Module is not a big deal"""
import json


def save_to_json_file(my_obj, filename):
    """who cares about a function"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
