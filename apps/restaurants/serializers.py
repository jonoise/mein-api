from rest_framework import serializers
from .models import Restaurant
from apps.plans.serializers import PlanSerializer


class CountingSerializer(serializers.Serializer):
    menus = serializers.IntegerField()
    tables = serializers.IntegerField()
    dishes = serializers.IntegerField()
    orders = serializers.IntegerField()
    total_last_month = serializers.IntegerField()
    total_last_week = serializers.IntegerField()


class RestaurantSerializer(serializers.ModelSerializer):
    _plan = PlanSerializer()
    _counting = CountingSerializer()

    class Meta:
        model = Restaurant
        fields = "__all__"
        extra_fields = ["_plan", "_counting"]
