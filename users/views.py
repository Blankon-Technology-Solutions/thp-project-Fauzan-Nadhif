from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer