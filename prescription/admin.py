from django.contrib import admin

from .models import Visit, Prescription, Dosage

# Register your models here.
admin.site.register(Visit)
admin.site.register(Prescription)
admin.site.register(Dosage)
