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
    duration = models.PositiveIntegerField(null=True, blank=True)
    calories = models.PositiveIntegerField(null=True, blank=True)
    is_veggie = models.BooleanField()
    is_gluten_free = models.BooleanField()

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self) -> str:
        return f'{self.name} del {self.menu}'


class Discount(models.Model):
    dish = models.OneToOneField(
        Dish, on_delete=models.CASCADE, related_name="discount")
    new_price = models.PositiveIntegerField()
    expires = models.DateField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()


class Specific(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="specifics")
    name = models.CharField(max_length=200)
    type_of = models.CharField(max_length=20)
    limit = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Specific for {self.dish}'

    def _options(self):
        return self.options.all()


class OptionField(models.Model):
    specific = models.ForeignKey(
        Specific, on_delete=models.CASCADE, related_name="options")
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'OptionField for {self.specific}'
