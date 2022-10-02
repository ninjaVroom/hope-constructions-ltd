"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD PARTY
    'django_crontab',
    'debug_toolbar',
    'rest_framework',
    "markdown",
    'django_filters',
    "django_hosts",
    "corsheaders",

    # MY LIBRARIES
    'cron_jobs',
    'Libraries',
    'hope_construction',

    # MY CREATED APPS
    'app_token_auth',
    'api',

]

CRONJOBS = [
#     ('* * * * *', 'cron_jobs.info_center.sender.info_center_now_sender.main.main'),
#     ('*/5 * * * *', 'cron_jobs.info_center.sender.info_center_scheduled_sender.main.main')
]

MIDDLEWARE = [

    "django_hosts.middleware.HostsRequestMiddleware", # MUST BE FIRST ALWAYS
    "corsheaders.middleware.CorsMiddleware",

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "django_hosts.middleware.HostsResponseMiddleware" # MUST BE LAST ALWAYS
]

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # '192.168.173.1',
    # ...
]

ROOT_URLCONF = 'backend.urls'
ROOT_HOSTCONF = 'backend.hosts'
DEFAULT_HOST = 'www'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# '%jux0i7sxj=h*6v1)j=o8$kr^%5iv#@c^t%qylfypx$yexepf&'

DATABASE_NAMES = [
    'default', 
]
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    DATABASE_NAMES[0]: {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': str(PROJECT_DIR / 'auth/mysql.db.conf'),
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    },
}
DATABASE_ROUTERS = [
    'Libraries.databases.db_1.Db1Router',
]


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    PROJECT_DIR / "website/public/static",
]

# python manage.py collectstatic
STATIC_ROOT = PROJECT_DIR / "website/public/static-files-cdn"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        # 'rest_framework.renderers.JSONRenderer',
        'Libraries.classes.api.renderer.json.json.JSONResponseRenderer',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_AUTHENTICATION_CLASSES': ('app_token_auth.auth.TokenAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

from datetime import timedelta
from rest_framework.settings import api_settings

REST_AtAUTH = {
  'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
#   'TOKEN_TTL': timedelta(hours=24*7),
  'TOKEN_TTL': timedelta(hours=24*100),
  'USER_SERIALIZER': 'app_token_auth.serializers.UserSerializer',
  'TOKEN_LIMIT_PER_USER': None,
  'AUTO_REFRESH': False,
}

DEFAULT_FILE_STORAGE = "storages.backends.sftpstorage.SFTPStorage"

SFTP_STORAGE_HOST = env('SFTP_STORAGE_HOST')
SFTP_STORAGE_ROOT = env('SFTP_STORAGE_ROOT')
SFTP_STORAGE_PARAMS = dict(
    port=env('SFTP_STORAGE_PORT'),
    username=env('SFTP_STORAGE_USERNAME'),
    password=env('SFTP_STORAGE_PASSWORD')
)
SFTP_STORAGE_INTERACTIVE = env('SFTP_STORAGE_INTERACTIVE')
MEDIA_URL = env('SFTP_STORAGE_MEDIA_URL')
