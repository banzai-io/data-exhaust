from django.test import TestCase
from api import factories


class OrganizationAPIKeyTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.api_key_obj, cls.key = factories.OrganizationAPIKeyFactory.create()

    def test_str(self) -> None:
        self.assertEqual(
            str(self.api_key_obj),
            f'API Key for {self.api_key_obj.entity_name}'
        )
