from apps.users.models import Account, MainUser
from rest_framework import views, response, status, permissions
from .models import Email_Validation
from django.shortcuts import get_object_or_404
# Create your views here.


class ValidateEmail(views.APIView):

    def get(self, request, validation_uuid, *args, **kwargs):
        validator = get_object_or_404(Email_Validation, uuid=validation_uuid)
        if validator.is_valid:
            return response.Response({"message": 'is_valid'}, status.HTTP_208_ALREADY_REPORTED)

        uuid_is_valid = validator.validate_uuid()
        if uuid_is_valid:
            validator.perform_validation()
            return response.Response({"message": 'is_valid'}, status.HTTP_200_OK)

        return response.Response({"message": 'invalid_uuid'}, status.HTTP_404_NOT_FOUND)


class ResendEmail(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        account = get_object_or_404(Account, user=request.user)
        account_email_validation = account.email_validation.get()
        if account_email_validation.is_valid:
            return response.Response({"message": "is_valid"}, status.HTTP_208_ALREADY_REPORTED)

        account_email_validation.refresh_uuid()
        account_email_validation.send_email()
        return response.Response({"message": "sent"}, status.HTTP_200_OK)
