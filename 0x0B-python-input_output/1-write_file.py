#!/usr/bin/python3
""" function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """ Returns number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_char_written = f.write(text)
        return num_char_written
