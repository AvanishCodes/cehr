from django.db import models

from patient.models import Patient
from doctor.models import Doctor
from address.models import Address
from medicine.models import MarketableMedicine
from .visit import Visit


class Prescription(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.RESTRICT)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    medicine = models.ForeignKey(MarketableMedicine, on_delete=models.RESTRICT)
    dosage = models.CharField(max_length=255)
