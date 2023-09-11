#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        """prints a sorted list of integers"""
        self.sort()
        print(self)
