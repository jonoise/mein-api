from rest_framework import generics
from .models import Category, Menu
from .serializers import MenuSerializer, CategorySerializer


class ListCreateMenus(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ListCreateCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetrieveUpdateDestroyMenus(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del Menu"""
    lookup_field = "uuid"
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RetrieveUpdateDestroyCategories(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del Category"""
    lookup_field = "uuid"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
