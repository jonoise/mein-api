from rest_framework import generics
from .models import Check
from .serializers import CheckSerializer


class ListCreateCheck(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class RetrieveUpdateDestroyCheck(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del Check"""
    lookup_field = "uuid"
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
