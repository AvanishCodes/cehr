from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def __str__(self):
        return f'{self.name}'


__all__ = (
    'Patient',
)
