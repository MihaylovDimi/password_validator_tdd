"""Password validator built with TDD."""


def validate(password):
    has_digit = any(char.isdigit() for char in password)
    return len(password) >= 8 and has_digit