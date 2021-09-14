from django.urls import path
from .views import ListCreateDishes, ListCreateSpecific, RetrieveUpdateDestroyDishes
urlpatterns = [
    path('', ListCreateDishes.as_view(), name="list-create-dishes"),
    path('specific/', ListCreateSpecific.as_view(), name="list-create-specific"),
    path('<str:uuid>/', RetrieveUpdateDestroyDishes.as_view(), name="rud-dishes"),
]
