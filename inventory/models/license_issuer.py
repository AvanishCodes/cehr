from django.db import models
from address.models import Address


class LicenseIssuer(models.Model):
    """A model for an entity that issues licenses."""

    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    phone_number = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    class Meta:
        verbose_name = "License Issuer"
        verbose_name_plural = "License Issuers"

    def __str__(self):
        return self.name


__all__ = ["LicenseIssuer"]