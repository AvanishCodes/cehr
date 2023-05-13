from django.db import models
from patient.models import Patient
from doctor.models import Doctor


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    datetime = models.DateTimeField(auto_now_add=True, blank=False, null=False)
