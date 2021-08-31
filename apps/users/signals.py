from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from apps.email_validation.models import Email_Validation
from uuid import uuid4


@receiver(post_save, sender=Account)
def createEmailValidation(sender, instance, created, **kwargs):
    if created:
        if instance.is_owner:
            newEmailVaidation = Email_Validation(
                account=instance, uuid=f'{uuid4()}-{uuid4()}')
            newEmailVaidation.save()
            newEmailVaidation.send_email()
