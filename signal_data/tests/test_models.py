from django.test import TestCase
from signal_data import factories


class DataSignalTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data_signal = factories.DataSignalFactory.create()

    def test_str(self) -> None:
        self.assertEqual(
            str(self.data_signal),
            f'{self.data_signal.signal_type} signal - {self.data_signal.valid}'
        )
