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
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
    )
    pincode = models.CharField(max_length=10)
