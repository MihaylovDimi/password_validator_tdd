def validate(password):
    has_digit = False

    for char in password:
        if char.isdigit():
            has_digit = True
            break
    return len(password) >= 8 and has_digit