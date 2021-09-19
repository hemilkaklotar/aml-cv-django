from django.contrib import admin
from hospital.models import Doctor,Patient,Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
