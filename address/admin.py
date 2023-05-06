from django.contrib import admin

# Register your models here.
from .models import City, State, Country, Address

admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Address)