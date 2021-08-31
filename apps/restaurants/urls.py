from apps.restaurants.views import ListCreateRestaurants, RetrieveUpdateDestroyRestaurants
from django.urls import path

urlpatterns = [
    path('', ListCreateRestaurants.as_view(), name="list-create-restaurant"),
    path('<str:uuid>',
         RetrieveUpdateDestroyRestaurants.as_view(), name="rud-restaurant")
]
