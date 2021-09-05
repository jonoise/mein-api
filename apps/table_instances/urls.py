from django.urls import path
from .views import TableInstaceAvailability, ListCreateTableInstance, DetailTableInstance, RejectTableInstace
urlpatterns = [
    path("", ListCreateTableInstance.as_view(),
         name="list-create-table_instance"),
    path("availability/", TableInstaceAvailability.as_view(),
         name="table-instance-availability"),
    path("reject/", RejectTableInstace.as_view(),
         name="table-instance-reject"),
    path("<str:uuid>/", DetailTableInstance.as_view(),
         name="table_instance-detail"),
]
