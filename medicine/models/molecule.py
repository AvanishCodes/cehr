# medicine/models/molecule.py
from django.db import models


class Molecule(models.Model):
    shorthand = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name