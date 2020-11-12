import factory
from django.db.models.signals import post_save, pre_save

from api.models import OrganizationAPIKey


@factory.django.mute_signals(post_save, pre_save)
class OrganizationAPIKeyFactory(factory.django.DjangoModelFactory):
    """Create test organization API Key."""
    class Meta:
        model = OrganizationAPIKey

    name = factory.Sequence(lambda n: "Company API Key {}".format(n))

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Create an instance of the key, and save it to the database,
        then return the key too.
        """
        manager = cls._get_manager(model_class)
        return manager.create_key(*args, **kwargs)
