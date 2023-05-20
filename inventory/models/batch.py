from django.db import models
from medicine.models import MarketableMedicine
from .packaging_unit import PackagingUnit


class MedicineBatch(models.Model):
    """A model for the details of a medicine batch."""

    medicine = models.ForeignKey(MarketableMedicine, on_delete=models.RESTRICT)
    manufacturer = models.CharField(max_length=255)
    expiration_date = models.DateField()
    batch_number = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(PackagingUnit, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Medicine Batch"
        verbose_name_plural = "Medicine Batches"

    def __str__(self):
        return f"{self.medicine_name} ({self.batch_number})"


__all__ = ["MedicineBatch"]