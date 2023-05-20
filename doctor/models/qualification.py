# doctor/models/qualification.py
from django.db import models

from .enums import QualificationType
from .specialization import Specialization


class Qualification(models.Model):
    name = models.CharField(max_length=100)
    qualification_type = models.CharField(
        max_length=20,
        choices=QualificationType.choices,
        default=QualificationType.OTHER,
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.RESTRICT,
        null=True,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name