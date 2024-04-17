from django.urls import path, include, re_path

from .views import ListTodo, DetailTodo, test_ws

urlpatterns = [
    path('', ListTodo.as_view(), name='todos-list'),
    path('<int:pk>/', DetailTodo.as_view(), name='todos-detail'),
    path('test-ws', test_ws, name='test-ws'),
    re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
]