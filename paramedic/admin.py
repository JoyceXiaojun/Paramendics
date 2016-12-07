from django.contrib import admin
from paramedic.models import Hospital
from paramedic.models import Patient
from paramedic.models import MedicalInstr

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(MedicalInstr)

