import uuid
from django.db import models
from apps.restaurants.models import Restaurant
from apps.checks.models import CheckedDish


class Kitchen(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="kitchens")
    uuid = models.CharField(max_length=255, default=uuid.uuid4)
    door = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'Cocina del {self.restaurant}'


class KitchenDish(models.Model):
    checkedDish = models.ForeignKey(
        CheckedDish, on_delete=models.CASCADE, related_name="kitchenDish")
    ordered = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField()
    finished = models.DateTimeField()

    def __str__(self) -> str:
        return f'KitchenDish from {self.checkedDish}'
