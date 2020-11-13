from rest_framework import serializers
from signal_data.models import DataSignal
from signal_data.utils import hash_identifier


class DataSignalSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSignal
        fields = [
            'signal_type',
            'identifier',
            'signal_value',
            'valid',
            'signal_meta',
            'added',
        ]

    def validate_identifier(self, value):
        if not value:
            raise serializers.ValidationError('This field is required')
        return hash_identifier(value)

