"""
Django settings for todo project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m3vfsz8nvs&l7^v9e-@sn@5d^6a7h81m(gda34c&i638622n5)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    "allauth",
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'users',
    'authentication',
    'todos',
]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = "todo.asgi.application"
WSGI_APPLICATION = 'todo.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  # Use In-Memory channel layer for development
    },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "Database.Engine.Not.Defined"),
        "HOST": os.environ.get("DB_HOST", "Database.Host.Not.Defined"),
        "PORT": int(os.environ.get("DB_PORT", "5432")),
        "NAME": os.environ.get("DB_NAME", "Database.Name.Not.Defined"),
        "USER": os.environ.get("DB_USERNAME", "Database.UserName.Not.Defined"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'



SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get(
                "GOOGLE_OAUTH2_CLIENT_ID", "Google.ClientID.Not.Defined"
            ),
            "secret": os.environ.get(
                "GOOGLE_OAUTH2_CLIENT_SECRET", "Google.ClientSecret.Not.Defined"
            ),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    },
    "linkedin": {
        "SCOPE": ["r_basicprofile", "r_emailaddress"],
        "PROFILE_FIELDS": [
            "id",
            "first-name",
            "last-name",
            "email-address",
            "picture-url",
            "public-profile-url",
        ],
    },
}

GOOGLE_OAUTH2_CALLBACK_URL = os.environ.get(
    "GOOGLE_OAUTH2_CALLBACK_URL", "Google.CallbackUrl.Not.Defined"
)

LINKEDIN_CALLBACK_URL = os.environ.get(
    "LINKEDIN_OAUTH2_CALLBACK_URL", "Linkedin.CallbackUrl.Not.Defined"
)

REST_AUTH = {
    "USE_JWT": True,
}

class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


TESTS_IN_PROGRESS = False
if 'test' in sys.argv[1:]:
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = DisableMigrations()