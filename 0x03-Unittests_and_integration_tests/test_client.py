#!/usr/bin/env python3
"""Test the client module"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import requests

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """class to test Org method"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, organization: str, mock: unittest.mock.patch):
        """
        method to test the Org request.
        Args:
            organisation (str):
            mock (any):
        return: nothing
        """
        testClass = GithubOrgClient.org(organization)
        testClass.org()
        mock.assert_called_once_with(
                f"https://api.github.com/orgs/{organization}"
                )

    def test_public_repos_url(self):
        """test the public repository"""
        with patch.object(
                GithubOrgClient, "org", newCallable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "test"}
            testClass = GithubOrgClient('test')
            res = testClass._public_repos_url
            self.assertEqual(res, mock.return_value['repos_url'])
