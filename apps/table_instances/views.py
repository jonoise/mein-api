from apps.table_instances.serializers import TableInstanceSerializer
from rest_framework import generics
from .models import TableInstance


class ListCreateTableInstance(generics.ListCreateAPIView):
    queryset = TableInstance.objects.all()
    serializer_class = TableInstanceSerializer


class DetailTableInstance(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "uuid"
    queryset = TableInstance.objects.all()
    serializer_class = TableInstanceSerializer
