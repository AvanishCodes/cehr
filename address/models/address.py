# Imports from Django
from django.db import models

# Imports from same submodule
from .city import City
from .state import State


class Address(models.Model):
    al1 = models.CharField(max_length=200)
    al2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True,
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        null=True,
    )
    pincode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.al1} {self.al2} {self.city.name} {self.state.name}'
