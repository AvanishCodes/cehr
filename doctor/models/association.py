# doctor/models/association.py
from django.db import models

from .enums import AsssociationType


class Association(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(
        max_length=7,
        choices=AsssociationType.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
