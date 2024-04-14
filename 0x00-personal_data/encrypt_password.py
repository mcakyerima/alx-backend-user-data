!/usr/bin/env python3
"""
Password encryption and decryption using bcrypt library
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the password against the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
