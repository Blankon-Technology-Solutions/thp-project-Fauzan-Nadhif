from django.urls import path

from .apis import GoogleLoginApi, GoogleLoginRedirectApi

app_name = 'authentication'
urlpatterns = [
    path('callback/', GoogleLoginApi.as_view(), name='callback'),
    path('redirect/', GoogleLoginRedirectApi.as_view(), name='redirect'),
]

