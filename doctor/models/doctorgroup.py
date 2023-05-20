# doctor/models/doctorgroup.py
from django.db import models

from address.models import Address


class DoctorGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.ForeignKey(
        Address,
        on_delete=models.RESTRICT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
