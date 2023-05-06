# doctor/models/specilization.py
from django.db import models


class Specialization(models.Model):
    shorthand = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
