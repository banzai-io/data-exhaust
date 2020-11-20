from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions

from signal_data.models import DataSignal
from signal_data.serializers import DataSignalSerializer

from api.permissions import HasInternalAPIKey


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
class PrivateDataSignalViewSet(viewsets.ModelViewSet):
    queryset = DataSignal.objects.all()
    serializer_class = DataSignalSerializer
    permission_classes = [permissions.IsAuthenticated | HasInternalAPIKey]
    lookup_field = 'uuid'
