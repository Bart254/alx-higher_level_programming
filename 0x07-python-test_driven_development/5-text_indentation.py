#!/usr/bin/python3
""" Idents sentences
"""


def text_indentation(text):
    """ Returns indented text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    newline_char = ['.', '?', ':']
    newline = True
    for char in text:
        if char == ' ' and newline:
            pass
        else:
            print(char, end="")
            if char in newline_char:
                print("\n"+"\n", end="")
                newline = True
            else:
                newline = False
