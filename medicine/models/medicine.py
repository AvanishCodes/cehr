# medicine/models/medicine.py
from django.db import models
from .marketer import Marketer
from .enums import MedicineType

class Medicine(models.Model):
    shorthand = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200)
    marketer = models.ForeignKey(Marketer, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20,
        choices=MedicineType.choices,
        default=MedicineType.OT,
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)