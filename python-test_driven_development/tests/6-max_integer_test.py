#!/usr/bin/python3
"""Unittest of max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_just_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_positive_elements(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_maxmiddle_elements(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_negative_elements(self):
        self.assertEqual(max_integer([-1, -2, -3, -5]), -1)

    def test_neg_pos_elements(self):
        self.assertEqual(max_integer([-1, 3, -1, 4]), 4)

    def empty_list(self):
        max_integer = None
        self.assertEqual(max_integer(), None)
    
    if __name__ == '__main__':
        unittest.main()