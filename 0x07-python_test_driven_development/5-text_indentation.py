#!/usr/bin/python3
""" Function Module
"""


def text_indentation(text):
    """ prints a text with two new line after any of characters . : ?
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    check_char = [':', '?', '.']
    e = 0
    while e < len(text):
        if e == 0 and text[e] == ' ':
            while text[e] == ' ':
                e += 1
        print(text[e], end="")
        if text[e] in check_char:
            print("\n\n", end="")
            e += 1
            if e < len(text):
                while text[e] == ' ':
                    e += 1
        else:
            e += 1
