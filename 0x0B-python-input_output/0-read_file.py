#!/usr/bin/python3
"""Module writes to the stdout
"""


def read_file(filename=""):
    """writes filename to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
