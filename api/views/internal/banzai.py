from rest_framework import viewsets


from signal_data.models import DataSignal
from signal_data.serializers import DataSignalSerializer

from api.permissions import HasInternalAPIKey


class PrivateDataSignalViewSet(viewsets.ModelViewSet):
    queryset = DataSignal.objects.all()
    serializer_class = DataSignalSerializer
    permission_classes = [HasInternalAPIKey]
