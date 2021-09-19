from django.urls import path
from .views import RetrieveKitchen
urlpatterns = [
    path("<str:rest_uuid>/", RetrieveKitchen.as_view(), name="retrieve_kitchen")
]
