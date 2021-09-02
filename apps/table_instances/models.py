from django.db import models
from apps.tables.models import Table


class TableInstance(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="instances")
    uuid = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)
