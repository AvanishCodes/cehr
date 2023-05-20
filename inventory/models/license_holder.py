from django.db import models
from .license_issuer import LicenseIssuer


class LicenseHolder(models.Model):
    """A model for a person to whom a license has been issued."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    license_issuer = models.ForeignKey(LicenseIssuer, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "License Holder"
        verbose_name_plural = "License Holders"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


__all__ = ["LicenseHolder"]