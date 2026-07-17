from django.db import models

from myasets.models.supplier import Supplier


class Asset(models.Model):
    ASSET_STATUS = (
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('in_maintenance', 'In Maintenance'),
        ('disposed', 'Disposed'),
    )

    name = models.CharField(max_length=150)
    asset_tag = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, related_name='assets',
        blank=True, null=True,
    )
    purchase_date = models.DateField(blank=True, null=True)
    purchase_cost = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
    )
    warranty_expiry = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=ASSET_STATUS, default='available',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name', 'asset_tag']

    def __str__(self):
        return f"{self.name} ({self.asset_tag})"
