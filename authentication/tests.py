from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

class BasicLoginViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='password123')

    def test_login_success(self):
        url = reverse('authentication:basic-login')

        data = {
            'username': 'testuser@gmail.com',
            'password': 'password123'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_login_fail(self):
        url = reverse('authentication:basic-login')

        data = {
            'username': 'testuser@gmail.com',
            'password': 'wrongpassword'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='password123')

    def test_register(self):
        url = reverse('authentication:register')

        data = {
            'email': 'testuser2@gmail.com',
            'password': 'password456',
            'confirm_password': 'password456'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='testuser2@gmail.com').exists())
    
    def test_register_fail_invalid_email(self):
        url = reverse('authentication:register')

        data = {
            'email': 'testuser2',
            'password': 'password456',
            'confirm_password': 'password456'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_register_fail_password_mismatch(self):
        url = reverse('authentication:register')

        data = {
            'email': 'testuser2',
            'password': 'password456',
            'confirm_password': 'password123'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
