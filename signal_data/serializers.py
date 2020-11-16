from rest_framework import serializers
from signal_data.models import DataSignal
from signal_data.utils import hash_identifier, snake_case


class DataSignalSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSignal
        fields = [
            'uuid',
            'signal_type',
            'identifier',
            'signal_value',
            'valid',
            'signal_meta',
            'added',
        ]

    def validate_identifier(self, value):
        """
        Hash the signal identifier (personal information) before sending to database to save or query existing data
        :param value: identifier coming from request
        :return: hashed identifier
        """
        if not value:
            raise serializers.ValidationError('This field is required')  # pragma: no cover
        elif not hash_identifier(value):
            raise serializers.ValidationError('Please supply a valid phone number')
        return hash_identifier(value)

    def validate_signal_value(self, value):
        """
        Convert the signal value to snake case (as it complies with the majority of our possible values)
        :param value: signal value coming from request
        :return: signal value converted to snake case
        """
        return snake_case(value)
