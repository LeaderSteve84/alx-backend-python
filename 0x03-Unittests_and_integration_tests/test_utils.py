#!/usr/bin/env python3
"""test utils.py module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """class to test access_nested_map method
    of utils.py
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expectedValue):
        """test for the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expectedValue)

    @parameterized.expand([
        ({}, ('a',), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expectedValue
            ):
        """test for access_nested_map_exception"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(error.exception), repr(expectedValue))


class TestGetJson(unittest.TestCase):
    """TestGetJson(unittest.TestCase) class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict):
        """unittest for correct execution"""
        with patch('requests.get') as mockRequest:
            mockRequest.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)
