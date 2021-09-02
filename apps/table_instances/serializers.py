from rest_framework import serializers
from .models import TableInstance


class TableInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInstance
        fields = "__all__"
