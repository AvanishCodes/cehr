from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, default=None, blank=True, )
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(
        User,
        on_delete=models.RESTRICT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self) -> str:
        name = self.first_name + ' ' + self.last_name
        return name

    def __str__(self):
        return f'{self.name}'


__all__ = (
    'Patient',
)
