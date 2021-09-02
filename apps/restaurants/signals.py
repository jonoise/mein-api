from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Restaurant


# POST INIT SLUG
@receiver(pre_save, sender=Restaurant)
def createFreshSlug(sender, instance, **kwargs):
    instance.create_slug()
