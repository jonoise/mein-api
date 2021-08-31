from rest_framework import generics
from .models import Dish
from .serializers import DishSerializer
# Create your views here.


class ListCreateDishes(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RetrieveUpdateDestroyDishes(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del Dish"""
    lookup_field = "uuid"
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
