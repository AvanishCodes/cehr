# doctor/models/membership.py
from django.db import models
from .doctor import Doctor
from .doctorgroup import DoctorGroup


class Membership(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete= models.RESTRICT
    )
    association = models.ForeignKey(
        DoctorGroup,
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
