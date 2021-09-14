from rest_framework import serializers
from .models import Restaurant
from apps.plans.serializers import PlanSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    _plan = PlanSerializer()

    class Meta:
        model = Restaurant
        fields = "__all__"
        extra_fields = "_plan"
