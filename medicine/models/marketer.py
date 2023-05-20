# medicine/models/marketer.py
from django.db import models
from address.models import Address


class Marketer(models.Model):
    shorthand = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200)
    address = models.ForeignKey(
        Address,
        on_delete=models.RESTRICT,
        null=True,
        default=None,
    )


    def __str__(self):
        return self.name