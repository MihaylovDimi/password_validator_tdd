"""Tests for the password validator."""

import unittest
from password_validator import validate


class TestPasswordValidator(unittest.TestCase):

    def test_empty_password_is_invalid(self):
        self.assertFalse(validate(""))


    def test_seven_character_password_is_invalid(self):
        self.assertFalse(validate("1234567"))

    def test_eight_character_password_is_valid(self):
        self.assertTrue(validate("12345678"))

    def test_password_without_digit_is_invalid(self):
        self.assertFalse(validate("PasswordNoDigit"))
