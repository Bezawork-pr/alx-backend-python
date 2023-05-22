#!/usr/bin/env python3
"""Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method returns
what it is supposed to"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock


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

    @parameterized.expand([
        ({}, ("a",), ),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, test, path):
        """Use the assertRaises context manager
        to test that a KeyError is raised"""
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """TestCase"""
    @patch('utils.requests')
    def test_get_json(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200 
        mock_response.json.return_value = {'value': 'hello world'}
        mock_requests.get.return_value = mock_response
        result = get_json('https://bezawork-pr.github.io/hello_world.html')
        self.assertEqual(result, {'value': 'hello world'})


if __name__ == "__main__":
    unittest.main()
