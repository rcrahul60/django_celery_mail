from atexit import register
from rest_framework.test import APITestCase,APIClient
from django.urls import reverse
from rest_framework import status


class UserSerailizerTestCase(APITestCase):
    #client=APIClient()
    def test_create_account(self):
        payload={
            'name':'john',
            'email':'john@mail.com',
            'password':'test@123'
        }
        response = self.client.post(reverse('register'),payload,format='json')
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)