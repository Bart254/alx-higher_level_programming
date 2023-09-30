#!/usr/bin/python3
"""function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Returns number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        nb = f.write(text)
        return nb
