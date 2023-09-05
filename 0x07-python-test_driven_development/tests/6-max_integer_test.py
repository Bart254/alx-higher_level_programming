#!/usr/bin/python3
""" Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    """ subclass of testcase
    """
    def test_max(self):
        """ asserts the accuracy of a function checking the largest
        integer of a function
        """
        self.assertEqual(max_integer([1, 2, 4, 6, 8]), 8)
        self.assertEqual(max_integer([-1, -2, 0]), 0)
        self.assertIs(max_integer([]), None)
