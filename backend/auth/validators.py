import re


def validate_email(email):
    regex = re.compile(r'[a-zA-Z][a-zA-Z0-9.-]+'
                       r'@[a-zA-Z0-9.-]+'
                       r'.[a-zA-Z]{2,}$')
    return bool(re.fullmatch(regex, email))


def validate_username(username):
    regex = re.compile(r'[a-zA-Z][a-zA-Z0-9]+')
    return bool(re.fullmatch(regex, username))


def is_too_short_username(username):
    return len(username) < 3


def are_same_passwords(password1, password2):
    return password1 == password2


def is_too_short_password(password):
    return len(password) < 8


def is_good_password(password: str):
    upper, lower, digit = False, False, False
    for symbol in password:
        if symbol.islower():
            lower = True
        elif symbol.isdigit():
            digit = True
        elif symbol.isupper():
            upper = True
    return {'upper': upper,
            'lower': lower,
            'digit': digit}
