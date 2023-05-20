from django.db import models


class PackagingUnit(models.Model):
    unit = models.CharField(max_length=50)
    quantity = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.unit