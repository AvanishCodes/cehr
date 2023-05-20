from django.db import models
from prescription.models import Visit
from .store import Store


class Bill(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.RESTRICT)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    additional_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.visit.patient} ({self.visit})"
