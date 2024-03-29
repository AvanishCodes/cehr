# doctor/models/doctor.py
from django.db import models
from django.contrib.auth.models import User

from .specialization import Specialization
from .qualification import Qualification


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(
        User,
        on_delete=models.RESTRICT,
    )
    reg_no = models.CharField(max_length=50)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.RESTRICT,
    )
    highest_qualification = models.ForeignKey(
        Qualification,
        on_delete=models.RESTRICT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def __str__(self):
        return f'Dr. {self.name}, {self.highest_qualification}'
