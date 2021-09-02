from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer


class ListCreateRestaurants(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RetrieveUpdateDestroyRestaurants(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del restaurant"""
    lookup_field = "slug"
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
