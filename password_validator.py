"""Password validator built with TDD."""

MINIMUM_LENGTH = 8
SPECIAL_CHARACTERS = "!@#$%^&*"


def has_minimum_length(password):
    return len(password) >= MINIMUM_LENGTH


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special_character(password):
    return any(char in SPECIAL_CHARACTERS for char in password)


def validate(password):
    return (
        has_minimum_length(password)
        and has_digit(password)
        and has_special_character(password)
    )