# medicine/models/composition.py
from django.db import models
from .enums import CompositionType, UnitType
from .formula_medicine import Formula
from .molecule import Molecule


class MedicineComposition(models.Model):
    formula = models.ForeignKey(
        Formula,
        on_delete=models.RESTRICT,
    )
    molecule = models.ForeignKey(
        Molecule,
        on_delete=models.RESTRICT,
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
        return f'{self.formula} {self.quantity} {self.unit}'
