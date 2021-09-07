from rest_framework import serializers
from .models import Menu, Category
from apps.dishes.serializers import DishSerializer


class CategorySerializer(serializers.ModelSerializer):
    _dishes = DishSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"
        extra_fields = ["_dishes"]


class MenuSerializer(serializers.ModelSerializer):
    _categories = CategorySerializer(many=True)

    class Meta:
        model = Menu
        fields = ["id", "uuid", "has_veggie", "_categories"]
