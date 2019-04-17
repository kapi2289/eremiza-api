from base64 import b64encode
from hashlib import sha1
from time import time

import jwt


def hash_password(password):
    return b64encode(sha1(password.encode()).digest()).decode()


def gen_jwt(email, password):
    current_time = int(time())
    return jwt.encode(
        {
            "iss": "https://terminal.eremiza.abakus.net.pl",
            "aud": "https://api.eremiza.abakus.net.pl",
            "sub": email,
            "exp": current_time + 180,
            "iat": current_time,
            "nbf": current_time - 60,
        },
        hash_password(password),
        algorithm="HS256",
    ).decode()
