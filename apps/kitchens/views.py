from rest_framework import views, response, permissions, status
from apps.restaurants.models import Restaurant


class RetrieveKitchen(views.APIView):
    """
    This view return the kitchen uuid to retrieve info from the socket server.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, rest_uuid):
        kitchen = Restaurant.objects.get(uuid=rest_uuid).kitchen
        return response.Response({"uuid": kitchen}, status=status.HTTP_200_OK)
