from rest_framework import generics
from .models import Table
from .serializers import TableSerializer


class ListCreateTables(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filterset_fields = ('restaurant',)


class RetrieveUpdateDestroyTables(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid de la mesa"""
    lookup_field = "uuid"
    queryset = Table.objects.all()
    serializer_class = TableSerializer
