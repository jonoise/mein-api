from django.db import models
from apps.tables.models import Table


class TableInstance(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="instances")
    uuid = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return f'Instance {self.id} - {self.table}'
