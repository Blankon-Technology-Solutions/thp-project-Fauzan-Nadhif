from django.urls import path

from .views import ListTodo, DetailTodo, test_ws

urlpatterns = [
    path('', ListTodo.as_view(), name='todos-list'),
    path('<int:pk>/', DetailTodo.as_view(), name='todos-detail'),
    path('test-ws', test_ws, name='test-ws'),
]