"""Password validator built with TDD."""

MINIMUM_LENGTH = 8


def has_minimum_length(password):
    return len(password) >= MINIMUM_LENGTH


def has_digit(password):
    return any(char.isdigit() for char in password)


def validate(password):
    return has_minimum_length(password) and has_digit(password)