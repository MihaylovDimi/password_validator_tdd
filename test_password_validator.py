"""Tests for the password validator."""

import unittest
from password_validator import validate


class TestPasswordValidator(unittest.TestCase):

    def test_empty_password_is_invalid(self):
        self.assertFalse(validate(""))