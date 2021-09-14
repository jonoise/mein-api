import datetime
from apps.restaurants.models import Restaurant
from apps.users.models import Account
from django.db import models

# Create your models here.


class Plan(models.Model):
    owner = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="plans")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="plans")
    type_of = models.CharField(max_length=20, default="free")
    pricing = models.PositiveIntegerField(default=0)
    paid_until = models.DateField()

    def is_active(self):
        today = datetime.date.today()
        return self.paid_until > today
