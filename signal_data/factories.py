import factory
from factory.fuzzy import FuzzyChoice
from django.db.models.signals import post_save, pre_save

from signal_data.models import DataSignal
from signal_data.utils import hash_identifier


@factory.django.mute_signals(post_save, pre_save)
class DataSignalFactory(factory.django.DjangoModelFactory):
    """Create test organization API Key."""
    class Meta:
        model = DataSignal

    signal_type = FuzzyChoice(choices=DataSignal.SIGNAL_TYPES, getter=lambda c: c[0])
    identifier = factory.Sequence(lambda n: hash_identifier(f'test_{n}@example.com'))
    signal_value = FuzzyChoice(choices=DataSignal.SIGNAL_OPTIONS, getter=lambda c: c[0])
    valid = FuzzyChoice(choices=(True, False,))
