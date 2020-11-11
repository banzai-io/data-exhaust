from rest_framework import serializers
from signal_data.models import DataSignal


class DataSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSignal
        fields = ['signal_type', 'hashed_identifier', 'signal_value', 'valid', 'signal_meta', 'added', ]
