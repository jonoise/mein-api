from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, serializers, views, status
from rest_framework.fields import CreateOnlyDefault
from .models import Account, MainUser
from .serializers import AccountSerializer, ChangePasswordSerializer, MainUserSerializer
from django.db.utils import IntegrityError


class MainUserView(generics.CreateAPIView):
    """
    Este request se hace con email & password. Si las credenciales son correctas, se retorna el account y los tokens.
    Sino, {"message": "already_exists"}, status.HTTP_406_NOT_ACCEPTABLE
    """

    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer

    def post(self, request):
        credentials = request.data
        try:
            new_owner = MainUser.objects.create_user(
                email=credentials['email'],
                password=credentials['password']
            )

            owner_account = Account(
                user=new_owner,
                uuid=new_owner.uuid,
                email=credentials['email'],
                name=credentials['email'].split("@")[0],
                is_owner=True
            )
            owner_account.save()

            serializer = AccountSerializer(owner_account)

            return response.Response({"message": "created", "account": serializer.data, 'tokens': new_owner.tokens()}, status.HTTP_201_CREATED)

        except IntegrityError:
            return response.Response({"message": "already_exists"}, status.HTTP_208_ALREADY_REPORTED)

        except KeyError as err:
            return response.Response({"message": f"missing_field: {err.__str__()}"}, status.HTTP_406_NOT_ACCEPTABLE)


class MainUserLogin(generics.CreateAPIView):
    """
    Este request se hace con email & password. Si las credenciales son correctas, se retorna el account y los tokens.
    Sino, {'message': 'invalid_credentials'}, HTTP_401_UNAUTHORIZED
    """

    serializer_class = MainUserSerializer

    def post(self, request):
        credentials = request.data
        user = authenticate(
            email=credentials['email'], password=credentials['password'])
        if user:
            serializer = AccountSerializer(user.account)
            return response.Response({'account': serializer.data, 'tokens': user.tokens()})

        return response.Response({'message': 'invalid_credentials'}, status.HTTP_401_UNAUTHORIZED)


class MainUserChangePassword(generics.CreateAPIView):

    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_uuid):
        credentials = request.data
        found = get_object_or_404(MainUser, uuid=user_uuid)
        user = authenticate(
            email=found.email, password=credentials['old_password'])
        if user:
            user.set_password(credentials['new_password'])
            user.save()
            return response.Response({"message": "password_changed"}, status.HTTP_200_OK)
        return response.Response({"message": 'invalid_credentials'}, status.HTTP_406_NOT_ACCEPTABLE)


class WaiterView(generics.CreateAPIView):
    """
    Este request se hace con email & password. Email Fake y password elegido por el dueño. Son las cuentas de los meseros. Regresa HTTP_200
    Sino, {"message": "already_exists"}, HTTP_406_NOT_ACCEPTABLE
    """

    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer
    permission_classes = [permissions.IsAuthenticated]

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
