#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with positive integers
        self.assertEqual(max_integer([2, 3, 8, 1]), 8)
        # Test with negative integers
        self.assertEqual(max_integer([-5, -2, -9]), -2)
        # Test with mixed positive and negative integers
        self.assertEqual(max_integer([-3, 4, 1, -2]), 4)
        # Test with one element
        self.assertEqual(max_integer([5]), 5)
        # Test with an empty list
        self.assertEqual(max_integer([]), None)
        # Test with repeated numbers
        self.assertEqual(max_integer([3, 3, 3]), 3)

if __name__ == "__main__":
    unittest.main()