from rest_framework import generics, permissions, parsers, status, views
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Restaurant
from .serializers import RestaurantSerializer
from uuid import uuid4


# class ListCreateRestaurants(generics.ListCreateAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer
#     permission_classes = [permissions.AllowAny]
#     filterset_fields = ["owner"]
#     parser_classes = [parsers.MultiPartParserError, parsers.FormParser]

class ListCreateRestaurants(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["owner"]
    parser_classes = [parsers.FormParser,
                      parsers.MultiPartParser]

    def get(self, request):
        q = Restaurant.objects.filter(owner=request.user.account)
        s = RestaurantSerializer(q, many=True)
        return Response(s.data)

    def post(self, request, format=None):
        data = request.data
        rest = Restaurant.objects.create(
            owner=request.user.account,
            uuid=uuid4(),
            name=data["name"],
            welcome_message=data["welcome_message"],
            type_of=data["type_of"],
            logo=data["logo"],
        )
        serializer = RestaurantSerializer(rest)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyRestaurants(generics.RetrieveUpdateDestroyAPIView):
    """NOTA PARA EL ENDPOINT: El parámetro uuid es el uuid del restaurant"""
    lookup_field = "uuid"
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
