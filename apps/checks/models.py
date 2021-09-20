from apps.restaurants.models import Restaurant
from django.db import models
from apps.tables.models import Table


class Check(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="checks")
    table = models.ForeignKey(
        Table, on_delete=models.DO_NOTHING, related_name="checks")
    uuid = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=20)
    was_split = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField()
    closed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Check de la {self.table} por {self.total_amount}'


class CheckedDish(models.Model):
    bill = models.ForeignKey(
        Check, on_delete=models.CASCADE, related_name="dishes")
    uuid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    specifics = models.TextField()

    def __str__(self) -> str:
        return f'Dish from {self.check}'
