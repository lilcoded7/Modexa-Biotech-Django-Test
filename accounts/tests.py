from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from accounts.views import CreateUser 
from rest_framework.test import APITestCase 
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from accounts import views
from rest_framework import status 
User = get_user_model()



class UserApiAuthenticationTest(SimpleTestCase):
    def test_get_user_is_resolve(self):
        url = reverse('register')
        url_view_function = resolve(url).func.view_class
        self.assertEquals(url_view_function, views.CreateUser)
        
class UserAPIView(APITestCase):
    url = reverse('register')
    
    def setUp(self):
        self.user = User.objects.create_user(email='admin@gmail.com', username='admin', password='thethethe')
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + str(self.token.access_token))
        self.data = {
            'username':'test',
            'email':'test@gmail.com',
            'phone':'2020000000',
            'password':'adminadmin'
        }
    # def test_register_user(self):
    #     response = self.client.post(self.url, self.data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_user_unauthenticated(self):
    #     self.client.force_authenticate(user=None, token=None)
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, 200)