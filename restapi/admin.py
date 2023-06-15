from django.contrib import admin
from restapi.models.patient_model import Patient

# Register your models here.



class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'contact', 'medical_history']



admin.site.register(Patient, PatientAdmin)