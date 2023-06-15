from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.



class UserRegistrationLoginTests(APITestCase):
    def test_user_registration(self):
        url = '/api/register/'
        data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'phone': '020000000',
            'password': 'thethethe',
            'password2': 'thethethe',
            
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'admin')

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='testpassword')

        url = '/api/login/'
        data = {
            'email': 'amdin@gmail.com',
            'password': 'thethethe'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)
