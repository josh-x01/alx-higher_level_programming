#!/usr/bin/python3
"""Module 1-write_file.
This module write text to the file.
"""


def write_file(filename="", text=""):
    """write_file functionn takes filename and
    text then add the text to filename

    Args:
        - filename: the file name
        - text: the text to be add
    """

    with open(filename, 'w', encoding="utf-8") as f:
        size_char = f.write(text)

    f.closed
    return size_char
