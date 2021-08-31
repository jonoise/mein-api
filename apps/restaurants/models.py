import os
from django.db import models
from apps.users.models import Account
# Create your models here.


def restaurante_logo_path(instance, filename):
    return os.path.join(
        'restaurants',
        instance.name,
        filename
    )


class Restaurant(models.Model):
    owner = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="restaurants")
    uuid = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    type_of = models.CharField(max_length=20, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True,
                             upload_to=restaurante_logo_path)
    main_menu = models.CharField(max_length=255, blank=True, null=True)
    max_tables = models.PositiveIntegerField(default=3)

    def __str__(self) -> str:
        return f'Restaurante {self.name}'
