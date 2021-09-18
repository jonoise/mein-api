import uuid
from django.db import models
from apps.restaurants.models import Restaurant


class Kitchen(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="kitchen")
    uuid = models.CharField(max_length=255, default=uuid.uuid4)
    door = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'Cocina del {self.restaurant}'
