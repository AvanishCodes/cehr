from django.contrib import admin
from .models import (
    MedicineBatch,
    Bill,
    LicenseHolder,
    LicenseIssuer,
    PackagingUnit,
    MedicineBatchSale,
    StoreStockQuantity,
    Store,
)

# Register your models here.
admin.site.register(MedicineBatch)
admin.site.register(Bill)
admin.site.register(LicenseHolder)
admin.site.register(LicenseIssuer)
admin.site.register(PackagingUnit)
admin.site.register(MedicineBatchSale)
admin.site.register(StoreStockQuantity)
admin.site.register(Store)

admin.site.site_title = "CEHR"
admin.site.site_header = "CEHR"
admin.site.index_title = "Admin Panel"
