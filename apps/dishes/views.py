from rest_framework import generics, permissions
from .models import Dish
from .serializers import DishSerializer, DishSpecificsSerializer
# Create your views here.


class ListCreateDishes(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RetrieveUpdateDestroyDishes(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del Dish"""
    lookup_field = "uuid"
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.AllowAny]


class ListCreateSpecific(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSpecificsSerializer
    permission_classes = [permissions.AllowAny]
