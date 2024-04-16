from django.urls import path

from todos.consumers import TodoConsumer

websocket_urlpatterns = [
    path("ws/todos/", TodoConsumer.as_asgi()),
]