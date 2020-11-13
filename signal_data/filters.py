from django_filters.rest_framework import FilterSet, CharFilter

from signal_data.models import DataSignal
from signal_data.utils import hash_identifier


class CustomDataSignalFilter(FilterSet):
    identifier = CharFilter(field_name='identifier', method='filter_by_encrypted_identifier')

    class Meta:
        model = DataSignal
        fields = ['signal_type', 'signal_value', 'valid',]

    def filter_by_encrypted_identifier(self, queryset, name, value):
        hashed_q_param = hash_identifier(value)
        if hashed_q_param:
            return queryset.filter(**{
                name: hashed_q_param
            })
        else:
            return queryset.none()