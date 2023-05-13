from django.db import models


class Dosage(models.Model):
    shorthand = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.shorthand} {self.description}'
