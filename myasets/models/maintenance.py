from django.db import models

from myasets.models.asset import Asset


class Maintenance(models.Model):
    MAINTENANCE_STATUS = (
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name='maintenance_records',
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    maintenance_date = models.DateField()
    cost = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
    )
    status = models.CharField(
        max_length=20, choices=MAINTENANCE_STATUS, default='scheduled',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-maintenance_date']

    def __str__(self):
        return f"{self.title} - {self.asset}"
