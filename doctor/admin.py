from django.contrib import admin

from .models import Doctor, Qualification, Specialization, Association, DoctorGroup, Membership, Venue, Sitting
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(Specialization)
admin.site.register(Association)
admin.site.register(DoctorGroup)
admin.site.register(Membership)
admin.site.register(Venue)
admin.site.register(Sitting)