from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from signal_data.models import DataSignal
from signal_data.serializers import DataSignalSerializer
from signal_data.filters import CustomDataSignalFilter

from api.permissions import HasOrganizationAPIKey

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

signal_type_param=openapi.Parameter(
    name='signal_type',
    in_="query",
    description="Choice of Email or Phone, depending on the identifier queried",
    required=False,
    type=openapi.TYPE_STRING
)

signal_value_param=openapi.Parameter(
    name='signal_value',
    in_="query",
    description="Identifier status (Optional)",
    required=False,
    type=openapi.TYPE_STRING
)

identifier_param=openapi.Parameter(
    name='identifier',
    in_="query",
    description="Raw identifier (phone or email) - will be hashed at destination. "
                "You can provide a comma-separated list of identifiers, and the results will include signals for all",
    required=True,
    type=openapi.TYPE_STRING
)

valid_param=openapi.Parameter(
    name='valid',
    in_="query",
    description='Specifies whether to search for valid or invalid identifier signals (Optional)',
    required=False,
    type=openapi.TYPE_BOOLEAN
)

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        manual_parameters=[
            identifier_param,
            signal_type_param,
            signal_value_param,
            valid_param,
        ]
    )
)
class PublicDataSignalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataSignal.objects.all()
    serializer_class = DataSignalSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CustomDataSignalFilter
    lookup_field = 'uuid'

    permission_classes = [permissions.IsAuthenticated | HasOrganizationAPIKey]
