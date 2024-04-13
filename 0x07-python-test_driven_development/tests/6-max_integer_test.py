#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
import sys
sys.path.append('..')
max_integer = __import__('6-max_integer').max_integer


class TextMaxInteger(unittest.TestCase):
    """ MaxInteger Testclass
    """
    def setUp(self):
        """Initializes lists to be assessed
        """
        self.list_a = [15, 34, 5, 2, 8]
        self.list_b = [-34, 5, 7, -9]
        self.list_c = [2.45, 56, 89]
        self.list_d = ['r', 5, 'tkhj', True]
        self.list_e = []
        self.list_f = [-1, -2, -5, -100]
        self.list_g = [23]
        self.list_h = None

    def test_max(self):
        """ Tests max_integer function
        """
        self.assertEqual(max_integer(self.list_a), 34)
        self.assertEqual(max_integer(self.list_b), 7)
        self.assertEqual(max_integer(self.list_c), 89)
        self.assertEqual(max_integer(self.list_f), -1)
        self.assertEqual(max_integer(self.list_g), 23)

        with self.assertRaises(Exception):
            max_integer(self.list_d)
        self.assertIs(max_integer(self.list_e), None)
        self.assertIs(max_integer(self.list_h), None)


if __name__ == "__main__":
    unittest.main()
