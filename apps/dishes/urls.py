from django.urls import path
from .views import ListCreateDishes, RetrieveUpdateDestroyDishes
urlpatterns = [
    path('', ListCreateDishes.as_view(), name="list-create-dishes"),
    path('<str:uuid>', RetrieveUpdateDestroyDishes.as_view(), name="rud-dishes"),
]
