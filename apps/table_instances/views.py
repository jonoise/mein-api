import uuid
from apps.tables.models import Table
from apps.table_instances.serializers import RejectInstanceSerializer, TableInstanceSerializer
from rest_framework import generics, response, permissions
from .models import TableInstance


class ListCreateTableInstance(generics.ListCreateAPIView):
    queryset = TableInstance.objects.all()
    serializer_class = TableInstanceSerializer


class DetailTableInstance(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "uuid"
    queryset = TableInstance.objects.all()
    serializer_class = TableInstanceSerializer


class TableInstaceAvailability(generics.CreateAPIView):
    queryset = TableInstance.objects.all()
    serializer_class = TableInstanceSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        table = Table.objects.get(uuid=request.data['table_uuid'])
        last_instance = table.instances.all().first()
        if last_instance:
            if last_instance.is_valid:
                return response.Response({
                    "uuid": last_instance.uuid,
                    "restaurant": {"id": table.restaurant.id, "slug": table.restaurant.slug},
                    "tableNumber": table.number,
                    "fresh": False
                })

        # CREAR UNA INSTANCIA NUEVA
        new_instance = TableInstance.objects.create(
            table=table,
            uuid=uuid.uuid4()
        )

        return response.Response({
            "uuid": new_instance.uuid,
            "restaurant": {"id": table.restaurant.id, "slug": table.restaurant.slug},
            "tableNumber": table.number,
            "fresh": True
        })


class RejectTableInstace(generics.CreateAPIView):
    queryset = TableInstance.objects.all()
    serializer_class = RejectInstanceSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        tableInstance = TableInstance.objects.get(
            uuid=request.data['instance_uuid'])
        if tableInstance:
            if tableInstance.is_valid:
                return response.Response({"reject": False})

        return response.Response({"reject": True})
