from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from restapi.models.patient_model import Patient



class PatientTestApi(APITestCase):

    def setUp(self):
        self.url = '/api/v1/register-patient/'
        self.data = {
            'name':'coded',
            'age':23,
            'gender':'male',
            'contact':'37748974893',
            'medical_history':'he is sick'
        }
    
    def test_patient_registration(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_retrive_patient_details(self):
        patient = Patient.objects.create(name='code', age=12, gender='male', contact='349483847', medical_history='he is not serious when sick')
        url = f'/api/v1/register-patient/{patient.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)