#!/usr/bin/env python3
"""Test the client module"""
import unnitest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import requests

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):

