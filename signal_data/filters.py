from django_filters.rest_framework import FilterSet, CharFilter

from signal_data.models import DataSignal
from signal_data.utils import hash_identifier


class CustomDataSignalFilter(FilterSet):
    identifier = CharFilter(field_name='identifier', method='filter_by_encrypted_identifier')

    class Meta:
        model = DataSignal
        fields = ['signal_type', 'signal_value', 'valid', ]

    def filter_by_encrypted_identifier(self, queryset, name, value):
        hashed_q_params = [hash_identifier(x) for x in value.split(',') if hash_identifier(x)]
        if len(hashed_q_params) > 1:
            return queryset.filter(**{
                name + '__in': hashed_q_params
            })
        elif len(hashed_q_params) == 1:
            return queryset.filter(**{
                name: hashed_q_params[0]
            })
        else:
            return queryset.none()
