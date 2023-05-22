#!/usr/bin/env python3
"""This file contains test classes"""
import unittest
from unittest.mock import patch
import client
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestCase"""
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mocked):
        """method test_org"""
        my_client = GithubOrgClient(org_name)
        my_client.org()
        string = "https://api.github.com/orgs/"
        mocked.assert_called_once_with(string + org_name)


if __name__ == "__main__":
    unittest.main()
