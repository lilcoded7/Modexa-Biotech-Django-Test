from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from restapi.models.patient_model import Patient 
from restapi.serializers import PatientSerializer

# Create your tests here.


class PatientViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('register-patient')
        self.valid_payload = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male',
            'contact':'0200000000',
            'medical_history':'admin is okay now'
        }

    def test_create_patient(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().name, 'John Doe')

    def test_retrieve_patient(self):
        patient = Patient.objects.create(name='Jane Smith', age=25, gender='Female')
        url = reverse('register-patient', kwargs={'pk': patient.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = PatientSerializer(patient)
        self.assertEqual(response.data, serializer.data)
