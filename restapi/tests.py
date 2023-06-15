from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from restapi.models.patient_model import Patient 
from restapi.serializers import PatientSerializer

# Create your tests here.



class PatientViewTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('register-patient')
        self.detail_url = reverse('register-patient', args=[1])
        self.data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male',
            'contact':'0200000000',
            'medical_history':'admin is okay now'
        }
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_patient(self):
        response = self.client.post(self.list_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().name, 'John Doe')

    def test_retrieve_patient(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = PatientSerializer(patient)
        self.assertEqual(response.data, serializer.data)

    def test_update_patient(self):
        patient = Patient.objects.create(name='Jane Smith', age=25, gender='Female')
        url = reverse('crude', args=[patient.id])
        updated_data = {
            'name': 'Jane Doe',
            'age': 30,
            'gender': 'Female',
            'contact':'020000009',
            'medical_history':'jane is sick'
        }
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        patient.refresh_from_db()
        self.assertEqual(patient.name, 'Jane Doe')

    def test_delete_patient(self):
        patient = Patient.objects.create(name='Jane Smith', age=25, gender='Female', contact='020000009', medical_history='jane is sick')
        url = reverse('crude', args=[patient.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)