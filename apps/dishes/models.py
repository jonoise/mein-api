from apps.menus.models import Category, Menu
from django.db import models


class Dish(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="dishes")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="dishes")
    uuid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    is_veggie = models.BooleanField()
    is_gluten_free = models.BooleanField()

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self) -> str:
        return f'{self.name} del {self.menu}'


# class CheckedDish(models.Model):
#     dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING)
#     quantity
#     class Meta:
#         verbose_name_plural = "Dishes"


class Discount(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="discount")
    new_price = models.PositiveIntegerField()
    expires = models.DateField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
