# Imports from Django
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    isd_code = models.CharField(max_length=200)
