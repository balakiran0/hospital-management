from django.contrib import admin
from .models import Patient, MedicalHistory

admin.site.register(Patient)
admin.site.register(MedicalHistory)
from django.contrib import admin
from .models import Appointment

admin.site.register(Appointment)