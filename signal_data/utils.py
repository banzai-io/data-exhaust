import hashlib

import phonenumbers
from django.conf import settings


def hash_identifier(value):
    if '@' not in value:
        try:
            parsed_num = phonenumbers.parse(value, 'US')
            if phonenumbers.is_possible_number(parsed_num):
                value = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.E164)
            else:
                return None
        except phonenumbers.phonenumberutil.NumberParseException:
            return None
    return hashlib.pbkdf2_hmac(
        'sha256',
        value.lower().encode(),
        settings.SECRET_KEY.encode(),
        10000
    ).hex()
