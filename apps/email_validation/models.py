import datetime as dt
from uuid import uuid4
from django.db import models
from apps.users.models import Account
from django.core.mail import send_mail
from django.conf import settings


class Email_Validation(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='email_validation')
    uuid = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'Email Validator for {self.account.email}'

    def validate_uuid(self):
        limit_date = self.last_updated + dt.timedelta(days=2)
        if dt.date.today() < limit_date:
            return True
        return False

    def perform_validation(self):
        self.is_valid = True
        self.save()
        return True

    # RESEND METHODS

    def refresh_uuid(self):
        newUUID = f'{uuid4()}-{uuid4()}'
        self.uuid = newUUID
        self.save()

    def send_email(self):
        send_mail("Email Verification",
                  f"Please validate your uuid: {self.uuid}", settings.EMAIL_HOST_USER, ['amilkarms@outlook.com'], fail_silently=False,)
