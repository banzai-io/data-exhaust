import typing

from django.http import HttpRequest
from rest_framework_api_key.permissions import BaseHasAPIKey
from api.models import OrganizationAPIKey


class HasOrganizationAPIKey(BaseHasAPIKey):
    model = OrganizationAPIKey


class HasInternalAPIKey(HasOrganizationAPIKey):

    def has_permission(self, request: HttpRequest, view: typing.Any) -> bool:
        assert self.model is not None, (
                "%s must define `.model` with the API key model to use"
                % self.__class__.__name__
        )
        key = self.get_key(request)
        if not key:
            return False
        return self.model.objects.is_valid(key) and self.model.objects.is_internal(key)
