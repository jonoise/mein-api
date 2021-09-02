from django.urls import path
from .views import ListCreateTableInstance, DetailTableInstance
urlpatterns = [
    path("", ListCreateTableInstance.as_view(),
         name="list-create-table_instance"),
    path("<str:uuid>", DetailTableInstance.as_view(),
         name="table_instance-detail"),
]
