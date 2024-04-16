from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Todo
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class TodoViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='password123')
        client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_todo_create(self):
        url = reverse('todos:todos-list')
        self.client.force_authenticate(self.user)

        data = {
            'title': 'Test Todo',
            'description': 'test description'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Todo.objects.filter(title='Test Todo').exists())

    def test_todo_list(self):
        url = reverse('todos:todos-list')
        self.client.force_authenticate(self.user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_detail(self):
        todo = Todo.objects.create(title='Test Todo', owner=self.user)
        url = reverse('todos:todos-detail', args=[todo.id])
        self.client.force_authenticate(self.user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_update(self):
        todo = Todo.objects.create(title='Test Todo', owner=self.user)
        url = reverse('todos:todos-detail', args=[todo.id])
        self.client.force_authenticate(self.user)

        data = {
            'title': 'Updated Todo',
            'description': 'Updated description'
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Todo.objects.filter(title='Updated Todo').exists())

    def test_todo_delete(self):
        todo = Todo.objects.create(title='Test Todo', owner=self.user)
        url = reverse('todos:todos-detail', args=[todo.id])
        self.client.force_authenticate(self.user)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Todo.objects.filter(title='Test Todo').exists())