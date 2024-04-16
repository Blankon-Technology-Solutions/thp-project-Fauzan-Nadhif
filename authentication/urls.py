from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import (
    BasicLoginView,
    LinkedinLoginView,
    GoogleLoginView,
    RegisterView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", BasicLoginView.as_view(), name="basic-login"),
    path("refresh-token/", TokenRefreshView.as_view(), name="token-refresh"),
    path("google/", GoogleLoginView.as_view(), name="google-login"),
    path("linkedin/", LinkedinLoginView.as_view(), name="linkedin-login"),
]
