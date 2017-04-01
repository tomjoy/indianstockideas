"""
Django settings for mysites project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l6ik-=6vy89i+%dk2s@cby4k_po^n(!g9^#_^1ehw#w_wtdw8$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.104','indianstockideas.in']


# Application definition

INSTALLED_APPS = [
   	'indianstockideas.apps.IndianstockideasConfig',
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

ROOT_URLCONF = 'mysites.urls'

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
                #'django.template.loaders.filesystem.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysites.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
 
    'default': {
 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
 
        'NAME': 'indianstockideas',
 
        'USER': 'postgres',
 
        'PASSWORD': 'root',
 
        'HOST': '',
 
        'PORT': '',
 
    }
 
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/indianstockideas/'

#################API##################################
USERNAME = "gittopaul2@gmail.com"
PASSWORD = "a12345"

SCREENER_LOGIN_URL = "https://www.screener.in/login/"
SCREENER_URL = "https://www.screener.in/api/screens/query/?query=Current+ratio+%3E+1.2+AND%0D%0AEPS+%3E+EPS+last+year+AND%0D%0ASales+last+year+%3E+Sales+preceding+year+AND%0D%0ANet+Profit+last+year+%3E+Net+Profit+preceding+year+AND%0D%0AMarket+Capitalization+%3E+5+AND%0D%0ANet+Profit++%3E+10+AND%0D%0ANet+Profit+last+year+%3E+5+AND%0D%0Acurrenttohigh+%3C+81"
NSE_URL = 'https://www.nseindia.com/content/historical/EQUITIES/2016/NOV/cm08NOV2016bhav.csv.zip'
