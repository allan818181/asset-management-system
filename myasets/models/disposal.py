from django.db import models

from myasets.models.asset import Asset


class Disposal(models.Model):
    DISPOSAL_METHOD = (
        ('sold', 'Sold'),
        ('donated', 'Donated'),
        ('recycled', 'Recycled'),
        ('scrapped', 'Scrapped'),
    )

    asset = models.OneToOneField(
        Asset, on_delete=models.CASCADE, related_name='disposal',
    )
    disposal_date = models.DateField()
    method = models.CharField(
        max_length=20, choices=DISPOSAL_METHOD, default='scrapped',
    )
    reason = models.TextField(blank=True, null=True)
    sale_value = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-disposal_date']

    def __str__(self):
        return f"{self.asset} - {self.method}"
