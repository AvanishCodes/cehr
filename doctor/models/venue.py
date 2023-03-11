# doctor/models/venue.py
from django.db import models

from address.models import Address

from .association import Association

class Venue(models.Model):
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )
    owner_group = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
