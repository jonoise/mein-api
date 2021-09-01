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
