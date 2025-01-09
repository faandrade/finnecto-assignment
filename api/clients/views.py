from finnecto.models import Client
from finnecto.serializers import ClientSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class ClientViewSet(ReadOnlyModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
