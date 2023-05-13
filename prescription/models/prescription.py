from django.db import models

from address.models import Address
from medicine.models import MarketableMedicine
from .visit import Visit
from .dosage import Dosage


class Prescription(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.RESTRICT)
    medicine = models.ForeignKey(MarketableMedicine, on_delete=models.RESTRICT)
    dosage = models.ForeignKey(Dosage, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.visit} prescribed {self.medicine}'
