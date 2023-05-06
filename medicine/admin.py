from django.contrib import admin
from .models import Marketer, Molecule, MarketableMedicine, MedicineComposition, Formula

# Register your models here.
admin.site.register(Marketer)
admin.site.register(Molecule)
admin.site.register(MarketableMedicine)
admin.site.register(Formula)
admin.site.register(MedicineComposition)
