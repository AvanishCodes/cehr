from django.contrib import admin
from .models import Marketer, Molecule, Medicine, MedicineComposition

# Register your models here.
admin.site.register(Marketer)
admin.site.register(Molecule)
admin.site.register(Medicine)
admin.site.register(MedicineComposition)
