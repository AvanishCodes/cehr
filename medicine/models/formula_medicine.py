# medicine/models/formula_medicine.py
from django.db import models
from .enums import MedicineType

class FormulaMedicine(models.Model):
    shorthand = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200)
    type = models.CharField(
        max_length=20,
        choices=MedicineType.choices,
        default=MedicineType.OTH,
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


__all__ = (
    FormulaMedicine,
)
