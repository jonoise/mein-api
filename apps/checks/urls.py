from django.urls import path
from .views import (
    ListCreateCheck,
    RetrieveUpdateDestroyCheck,
)
urlpatterns = [
    # CHECK
    path('', ListCreateCheck.as_view(), name="list-create-check"),
    path('<str:uuid>/', RetrieveUpdateDestroyCheck.as_view(), name="rud-checks"),
]
