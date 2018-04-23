"""
Django settings for patent_query_extender project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=5+^z+kr*1vhm81d(z9#j*1lhq9$4&*+w+*dyylfrhpqoez(qt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'patent-query-extender-dev.us-west-2.elasticbeanstalk.com',
]


# Application definition

INSTALLED_APPS = [
    'extender',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'patent_query_extender.urls'

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

WSGI_APPLICATION = 'patent_query_extender.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

ENV_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media')  ## user upload to this place
print(MEDIA_ROOT)

# import django_heroku 
# django_heroku.settings(locals())

# import json
# if 'AWS_ACCESS_KEY_ID' in os.environ:
#     pwd_data = {
#         "AWS_ACCESS_KEY_ID":os.environ['AWS_ACCESS_KEY_ID'],
#         "AWS_SECRET_ACCESS_KEY":os.environ['AWS_SECRET_ACCESS_KEY'],
#         "S3_BUCKET":os.environ['S3_BUCKET']
#     }
# else:
#     with open(os.path.join(BASE_DIR, 'pwd.json')) as f:
#         pwd_data = json.load(f)
    
# AWS_ACCESS_KEY_ID = pwd_data['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = pwd_data['AWS_SECRET_ACCESS_KEY']
# S3_BUCKET = pwd_data['S3_BUCKET']