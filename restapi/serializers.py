from rest_framework import serializers 
from restapi.models.patient_model import Patient



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"