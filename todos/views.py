from django.shortcuts import render
from rest_framework import generics, permissions

from .permissions import IsOwner
from .serializers import TodoSerializer
from todos import models

class ListTodo(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self, *args, **kwargs):
        return models.Todo.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self, *args, **kwargs):
        return models.Todo.objects.all().filter(owner=self.request.user)

def test_ws(request):
    return render(request, template_name='test-ws.html')