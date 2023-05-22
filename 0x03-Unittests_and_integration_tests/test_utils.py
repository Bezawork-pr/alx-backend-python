#!/usr/bin/env python3
"""Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method returns
what it is supposed to"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, test, path, answer):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(test, path), answer)


if __name__ == "__main__":
    unittest.main()
