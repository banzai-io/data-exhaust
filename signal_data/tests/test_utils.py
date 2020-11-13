import unittest
from signal_data.utils import hash_identifier


class IdentifierHasherTest(unittest.TestCase):

    def test_email_ident(self):
        test_email = 'test@example.com'
        self.assertNotEqual(hash_identifier(test_email), test_email)

    def test_phone_ident(self):
        test_phone = '+12345678901'
        self.assertNotEqual(hash_identifier(test_phone), test_phone)

    def test_invalid_phone(self):
        invalid_ident = '12345'
        self.assertIsNone(hash_identifier(invalid_ident))

    def test_invalid_ident(self):
        invalid_ident = 'invalid test ident'
        self.assertIsNone(hash_identifier(invalid_ident))
