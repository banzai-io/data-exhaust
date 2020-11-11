from rest_framework import viewsets
from rest_framework import permissions
from signal_data.models import DataSignal
from signal_data.serializers import DataSignalSerializer


class DataSignalViewSet(viewsets.ModelViewSet):
    queryset = DataSignal.objects.all()
    serializer_class = DataSignalSerializer
    permission_classes = [permissions.AllowAny]
