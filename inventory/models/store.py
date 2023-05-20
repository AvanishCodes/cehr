from django.db import models
from .license_issuer import LicenseIssuer
from .license_holder import LicenseHolder


class Store(models.Model):
    """A model for a store to which a license has been issued."""

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    license_issuer = models.ForeignKey(LicenseIssuer, on_delete=models.RESTRICT)
    license_holder = models.ForeignKey(LicenseHolder, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name
