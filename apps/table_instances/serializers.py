from rest_framework import serializers
from .models import TableInstance
from apps.tables.serializers import TableSerializer


class TableInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInstance
        fields = ['table']


class RejectInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInstance
        fields = ['uuid']
