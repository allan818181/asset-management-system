from django.db import models

from myasets.models.asset import Asset
from myasets.models.employee import Employee
from myasets.models.location import Location


class AssetAssignment(models.Model):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name='assignments',
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, related_name='assignments',
        blank=True, null=True,
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name='assignments',
        blank=True, null=True,
    )
    assigned_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-assigned_date']

    def __str__(self):
        return f"{self.asset} -> {self.employee or self.location}"
