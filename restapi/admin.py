from django.contrib import admin
from restapi.models.contact_model import Contact
from restapi.models.gender_model import Gender
from restapi.models.patient_model import Patient

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'number']

class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'contact', 'medical_history']




admin.site.register(Contact, ContactAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Patient, PatientAdmin)