import hashlib
from django.conf import settings


def hash_identifier(value):
    return hashlib.pbkdf2_hmac(
        'sha256',
        value.lower().encode(),
        settings.SECRET_KEY.encode(),
        10000
    ).hex()
