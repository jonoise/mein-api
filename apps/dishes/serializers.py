from rest_framework import serializers
from .models import Dish, OptionField, Specific


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class SpecificOptionFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionField
        fields = "__all__"


class DishSpecificsSerializer(serializers.ModelSerializer):
    _options = SpecificOptionFieldSerializer(many=True)

    class Meta:
        model = Specific
        fields = "__all__"
        extra_fields = ["_options"]
