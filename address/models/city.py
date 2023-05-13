# Imports from Django
from django.db import models

# Imports from same submodule
from .country import Country
from .state import State


class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        null=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} - {self.state.name} - {self.country.name}'
