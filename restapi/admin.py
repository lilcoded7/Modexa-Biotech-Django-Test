from django.contrib import admin
from restapi.models.gender_model import Gender
from restapi.models.patient_model import Patient

# Register your models here.




class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'contact', 'medical_history']




admin.site.register(Gender, GenderAdmin)
admin.site.register(Patient, PatientAdmin)