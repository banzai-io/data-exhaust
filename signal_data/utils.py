import hashlib
import re
import unicodedata

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


def snake_case(value, allow_unicode=False):
    """
        Convert to ASCII if 'allow_unicode' is False. Convert spaces to underscores.
        Remove characters that aren't alphanumerics, underscores, or hyphens.
        Convert to lowercase. Also strip leading and trailing whitespace.
        """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower()).strip()
    return re.sub(r'[-\s]+', '_', value)
