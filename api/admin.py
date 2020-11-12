from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin

from .models import OrganizationAPIKey


@admin.register(OrganizationAPIKey)
class OrganizationAPIKeyAdmin(APIKeyModelAdmin):
    list_display = ['entity_name', 'name', 'internal', ]
