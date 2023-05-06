# Imports from Django
from django.db import models
from .country import Country

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    shorthand = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.shorthand} - {self.name} - {self.country.name}'
