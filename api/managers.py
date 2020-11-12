from rest_framework_api_key.models import APIKeyManager


class OrganizationAPIKeyManager(APIKeyManager):

    def is_internal(self, key: str) -> bool:
        try:
            api_key = self.get_from_key(key)
        except self.model.DoesNotExist:
            return False

        if api_key.internal:
            return True

        return False
