from django.urls import path
from .views import ListCreateTables, RetrieveUpdateDestroyTables
urlpatterns = [
    path('', ListCreateTables.as_view(), name="list-create-restaurant"),
    path('<str:uuid>',
         RetrieveUpdateDestroyTables.as_view(), name="rud-restaurant")
]
