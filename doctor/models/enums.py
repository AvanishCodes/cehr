# doctor/models/enums.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Day(models.TextChoices):
    MON = 'MON', _('Monday')
    TUE = 'TUE', _('Tuesday')
    WED = 'WED', _('Wednesday')
    THU = 'THU', _('Thursday')
    FRI = 'FRI', _('Friday')
    SAT = 'SAT', _('Saturday')
    SUN = 'SUN', _('Sunday')


class AsssociationType(models.TextChoices):
    GOVT = 'GOVT', _('Government')
    PRIVATE = 'PRIVATE', _('Private')
    NGO = 'NGO', _('NGO')
    OTH = 'OTHER', _('Other')


class QualificationType(models.TextChoices):
    BACHELORS = 'BACHELORS', _('BACHELORSs')
    MASTERS = 'MASTERS', _('Masters')
    DOCTORATE = 'DOCTORATE', _('Doctorate')
    DIPLOMA = 'DIPLOMA', _('Diploma')
    CERTIFICATE = 'CERTIFICATE', _('Certificate')
    PRACTICE = 'PRACTICE', _('Practice')
    OTHER = 'OTHER', _('Other')
