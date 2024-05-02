import os
import hashlib


async def generating_hash(password):
    salt = os.urandom(16).hex()
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
    result = key+salt
    return result


async def is_valid_password(password, password_hash):
    hashed_pass = password_hash[:64]
    salt = password_hash[-32:]
    result = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
    if result == hashed_pass:
        return True
    return False
