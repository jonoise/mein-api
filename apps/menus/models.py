import os
from django.db import models
from apps.restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menus')

    uuid = models.CharField(max_length=255)
    has_veggie = models.BooleanField(default=False)
    has_gluten_freen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Menu de {self.restaurant}'

    def _categories(self):
        return self.categories.all()
        pass


def category_image_path(instance, filename):
    return os.path.join(
        'restaurants',
        instance.name,
        filename
    )


class Category(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='categories')

    uuid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to=category_image_path)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f'Categoria {self.name} del {self.menu}'

    def _dishes(self):
        return self.dishes.all()
