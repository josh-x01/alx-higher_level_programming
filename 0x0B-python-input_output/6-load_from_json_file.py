#!/usr/bin/python3
"""Module is not a big deal"""
import json


def load_from_json_file(filename):
    """who cares about a function"""
    with open(filename) as f:
        return json.load(f)
