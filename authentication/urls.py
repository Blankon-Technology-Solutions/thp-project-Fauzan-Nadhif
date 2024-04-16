from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import (
    BasicLoginView,
    LinkedinLoginView,
    GoogleLoginView,
    RegisterView,
)

urlpatterns = [
    path("auth-token/", BasicLoginView.as_view(), name="token_obtain_pair"),
    path("refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("google/", GoogleLoginView.as_view(), name="google_login"),
    path("linkedin/", LinkedinLoginView.as_view(), name="linkedin_login"),
]
