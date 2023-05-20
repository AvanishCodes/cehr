from django.db import models
from .store import Store
from .batch import MedicineBatch


class StoreStockQuantity(models.Model):
    """A model for the stock of an entity."""

    medicine_batch = models.ForeignKey(MedicineBatch, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Store Stock Quantity"
        verbose_name_plural = "Store Stock Quantities"

    def __str__(self):
        return f"{self.medicine_name} ({self.quantity})"


__all__ = ["StoreStockQuantity"]