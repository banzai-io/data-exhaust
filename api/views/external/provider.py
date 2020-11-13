from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from signal_data.models import DataSignal
from signal_data.serializers import DataSignalSerializer
from signal_data.filters import CustomDataSignalFilter

from api.permissions import HasOrganizationAPIKey


class PublicDataSignalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataSignal.objects.all()
    serializer_class = DataSignalSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CustomDataSignalFilter

    permission_classes = [permissions.IsAuthenticated | HasOrganizationAPIKey]
