# medicine/models/composition.py
from django.db import models
from .enums import CompositionType, UnitType
from .marketable_medicine import MarketableMedicine
from .molecule import Molecule


class MedicineComposition(models.Model):
    formula_medicine = models.ForeignKey(
        MarketableMedicine,
        on_delete=models.CASCADE,
    )
    molecule = models.ForeignKey(
        Molecule,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=3,
        choices=CompositionType.choices,
        default=CompositionType.WW,
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(
        max_length=3,
        choices=UnitType.choices,
        default=UnitType.MG,
    )

    def __str__(self):
        return f'{self.quantity} {self.unit}'
