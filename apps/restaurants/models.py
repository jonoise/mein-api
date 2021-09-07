import os
import random
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
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    welcome_message = models.CharField(max_length=105, blank=True, null=True)
    type_of = models.CharField(max_length=20, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True,
                             upload_to=restaurante_logo_path)
    main_menu = models.CharField(max_length=255, blank=True, null=True)
    max_tables = models.PositiveIntegerField(default=3)

    def __str__(self) -> str:
        return f'Restaurante {self.name}'

    def create_slug(self):
        if self.slug:
            return None
        newSlug = "-".join(self.name.lower().split(" "))
        try:
            self.__class__.objects.get(slug=newSlug)
            self.slug = newSlug + f'-{random.randint(1, 100)}'
        except:
            self.slug = newSlug
