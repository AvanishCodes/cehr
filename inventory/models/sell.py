from django.db import models
from .batch import MedicineBatch
from .bill import Bill


class MedicineBatchSale(models.Model):
    """A model for the sell of a MedicineBatch."""
    bill = models.ForeignKey(Bill, on_delete=models.RESTRICT)
    medicine_batch = models.ForeignKey(MedicineBatch, on_delete=models.RESTRICT)
    quantity_sold = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Medicine Batch Sale"
        verbose_name_plural = "Medicine Batch Sales"

    def __str__(self):
        return f"{self.medicine_batch} ({self.quantity_sold})"
