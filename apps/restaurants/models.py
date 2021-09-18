import os
import random
import datetime as dt
from django.db import models
from apps.users.models import Account
from django.db.models import Sum
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
    slug = models.SlugField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    welcome_message = models.CharField(max_length=145, blank=True, null=True)
    type_of = models.CharField(max_length=20, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True,
                             upload_to=restaurante_logo_path)
    main_menu = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

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

    def _plan(self):
        return self.plans.all().first()

    def get_dishes(self):
        if self.main_menu:
            menu = self.menus.all().get(uuid=self.main_menu)
            dishes = menu.dishes.all()
            return dishes
        return []

    def _counting(self):
        today = dt.date.today()
        a_month_ago = dt.timedelta(30)
        last_week = dt.timedelta(7)
        return {
            "menus": self.menus.count(),
            "tables": self.tables.count(),
            "dishes": len(self.get_dishes()),
            "orders": self.checks.count(),
            "total_last_month": self.checks.filter(created__gt=(today - a_month_ago)).aggregate(Sum("total_amount"))["total_amount__sum"],
            "total_last_week": self.checks.filter(created__gt=(today - last_week)).aggregate(Sum("total_amount"))["total_amount__sum"],
        }
