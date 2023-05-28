from django.db import models
from address.models import Address


class LicenseIssuer(models.Model):
    """A model for an entity that issues licenses."""

    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "License Issuer"
        verbose_name_plural = "License Issuers"

    def __str__(self):
        return self.name


__all__ = ["LicenseIssuer"]
