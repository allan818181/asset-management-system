from django.contrib import admin

from myasets.models import (
    Department,
    Employee,
    Supplier,
    Location,
    Asset,
    AssetAssignment,
    Maintenance,
    Disposal,
)

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Supplier)
admin.site.register(Location)
admin.site.register(Asset)
admin.site.register(AssetAssignment)
admin.site.register(Maintenance)
admin.site.register(Disposal)
