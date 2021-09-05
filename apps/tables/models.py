from django.db import models
from apps.restaurants.models import Restaurant


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="tables")
    uuid = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    seats = models.PositiveIntegerField(blank=True, null=True)
    show_seats = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Mesa {self.id} del {self.restaurant}'
