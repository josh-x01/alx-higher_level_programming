#!/usr/bin/python3
"""Module 2-append_write..
append text at the end of a file
"""


def append_write(filename="", text=""):
    """append_write functionn takes filename and
    text then add the text to filename at the end

    Args:
        - filename: the file name
        - text: the text to be add
    """

    with open(filename, 'a', encoding="utf-8") as f:
        size_char = f.write(text)

    return size_char
