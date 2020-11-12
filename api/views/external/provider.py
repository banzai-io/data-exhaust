from rest_framework import viewsets, permissions
from signal_data.models import DataSignal
from signal_data.serializers import DataSignalSerializer

from api.permissions import HasOrganizationAPIKey


class PublicDataSignalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataSignal.objects.all()
    serializer_class = DataSignalSerializer
    permission_classes = [permissions.IsAuthenticated | HasOrganizationAPIKey]
