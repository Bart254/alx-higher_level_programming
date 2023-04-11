#!/usr/bin/python3
"""Creates a subclass of list
"""


class MyList(list):
    """a list derived class"""
    def print_sorted(self):
        """prints a list object in sorted order"""
        print(self.sort())
