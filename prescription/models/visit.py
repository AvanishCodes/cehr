from django.db import models
from datetime import datetime as dt

from patient.models import Patient
from doctor.models import Doctor
from address.models import Address


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, null=True)
    datetime = models.DateTimeField(default=dt.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.name} visited {self.doctor.name} on {self.datetime}UTC'
