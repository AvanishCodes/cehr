# medicine/models/enums.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class MedicineType(models.TextChoices):
    TAB = 'TAB', _('Tablet')
    CAP = 'CAP', _('Capsule')
    SYP = 'SYP', _('Syrup')
    INJ = 'INJ', _('Injectable')
    OINT = 'OINT', _('Ointment')
    PWDR = 'PWDR', _('Powder')
    DROP = 'DROP', _('Drops')
    INV = 'INV', _('Intravenous')
    INH = 'INH', _('Inhaler')
    GEL = 'GEL', _('Gel')
    LOT = 'LOT', _('Lotion')
    SPRY = 'SPRY', _('Spray')
    PAST = 'PAST', _('Paste')
    OTH = 'OTH', _('Other')


class CompositionType(models.TextChoices):
    WW = 'WW', _('Weight to Weight')
    WV = 'WV', _('Weight to Volume')
    VW = 'VW', _('Volume to Weight')
    VV = 'VV', _('Volume to Volume')
    W = 'W', _('Weight')
    V = 'V', _('Volume')


class UnitType(models.TextChoices):
    MG = 'MG', _('Milligram')
    GM = 'GM', _('Gram')
    KG = 'KG', _('Kilogram')
    ML = 'ML', _('Milliliter')
    L = 'L', _('Liter')
    OTH = 'OTH', _('Other')


__all__ = (
    MedicineType,
    CompositionType,
    UnitType,
)
