# medicine/models/marketable_medicine.py
from django.db import models
from .marketer import Marketer

class MarketableMedicine(models.Model):
    shorthand = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200)
    marketer = models.ForeignKey(Marketer, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} ({self.marketer})'


__all__ = (
    MarketableMedicine,
)
