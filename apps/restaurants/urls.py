from django.urls import path
from .views import ListCreateRestaurants, RetrieveUpdateDestroyRestaurants

urlpatterns = [
    path('', ListCreateRestaurants.as_view(), name="list-create-restaurant"),
    path('<str:uuid>',
         RetrieveUpdateDestroyRestaurants.as_view(), name="rud-restaurant")
]
