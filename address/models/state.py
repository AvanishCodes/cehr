# Imports from Django
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)
    shorthand = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.shorthand} - {self.name}'
