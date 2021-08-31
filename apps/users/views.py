from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, serializers, views, status
from rest_framework.fields import CreateOnlyDefault
from .models import Account, MainUser
from .serializers import AccountSerializer, ChangePasswordSerializer, MainUserSerializer
from django.db.utils import IntegrityError


class MainUserView(generics.CreateAPIView):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer

    def post(self, request):
        credentials = request.data
        print(credentials)
        try:
            new_owner = MainUser.objects.create_user(
                email=credentials['email'],
                password=credentials['password']
            )

            owner_account = Account(
                user=new_owner,
                uuid=new_owner.uuid,
                email=credentials['email'],
                name=credentials['email'].split()[0],
                is_owner=True
            )
            owner_account.save()

            serializer = AccountSerializer(owner_account)

            return response.Response({"user": serializer.data, 'tokens': new_owner.tokens()}, status.HTTP_201_CREATED)
        except IntegrityError:
            return response.Response({"message": "already_exists"}, status.HTTP_406_NOT_ACCEPTABLE)


class WaiterView(generics.CreateAPIView):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer

    def post(self, request):
        credentials = request.data
        try:
            new_waiter = MainUser.objects.create_user(
                email=credentials['email'], password=credentials['password'])

            waiter_account = Account(
                user=new_waiter, name="Mesero", is_waiter=True, email=new_waiter.email)
            waiter_account.save()

            return response.Response({"message": "created"}, status.HTTP_201_CREATED)
        except IntegrityError:
            return response.Response({"message": "already_exists"}, status.HTTP_406_NOT_ACCEPTABLE)


class MainUserLogin(generics.CreateAPIView):

    serializer_class = MainUserSerializer

    def post(self, request):
        credentials = request.data
        user = authenticate(
            email=credentials['email'], password=credentials['password'])
        if user:
            serializer = AccountSerializer(user.account)
            return response.Response({'user': serializer.data, 'tokens': user.tokens()})

        return response.Response({'message': 'invalid_credentials'}, status.HTTP_401_UNAUTHORIZED)


class MainUserChangePassword(generics.CreateAPIView):

    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, uuid):
        credentials = request.data
        found = get_object_or_404(MainUser, uuid=uuid)
        user = authenticate(
            email=found.email, password=credentials['old_password'])
        if user:
            user.set_password(credentials['new_password'])
            user.save()
            return response.Response({"message": "password_changed"}, status.HTTP_200_OK)
        return response.Response({"message": 'invalid_credentials'}, status.HTTP_406_NOT_ACCEPTABLE)
