#!/usr/bin/python3
"""Module 0-read_file.
This module read text from file
"""


def read_file(filename=""):
    """read_file functionn takes filename and
    read text

    Args:
        - filename: the file name
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
