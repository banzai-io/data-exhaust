from django.db import models
from rest_framework_api_key.models import AbstractAPIKey

from api.managers import OrganizationAPIKeyManager


class OrganizationAPIKey(AbstractAPIKey):
    objects = OrganizationAPIKeyManager()

    entity_name = models.CharField(
        max_length=120,
        help_text='Name of organization for API Key '
                  '(Or application within organization)'
    )
    internal = models.BooleanField(
        default=False,
        help_text='Determines whether their key '
                  'has access to create exhaust data'
    )

    def __str__(self):
        return f'API Key for {self.entity_name}'
