# doctor/models/sitting.py
from django.db import models

from .enums import Day

from .doctor import Doctor
from .venue import Venue

class Sitting(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
    )
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
    )
    day = models.CharField(
        max_length=3,
        choices=Day.choices,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.doctor} at {self.venue} from {self.start_time} to {self.end_time}'
