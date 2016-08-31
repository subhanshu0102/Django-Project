"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(%^=n1p3k-x6pz1+o^96i3p+bc+4&i++#xva5@n3bbc+(%l1sy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False





#Some Predefined Settings of GRAPPELLI APP. 
GRAPPELLI_ADMIN_TITLE = 'Chhatrapati Shivaji Institute Of Technology '
GRAPPELLI_SWITCH_USER = True


"""
If running in Local Machine ALLOWED_HOSTS = [], This is the default Settings.

If running in Server or Production Version ALLOWED_HOSTS = ['*']

"""

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'grappelli',   #Make sure this should be above Admin App to override its UI settings.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csit', # CSIT App
     
    
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

ROOT_URLCONF = 'mysite.urls'  # Main URL's which Django should use.

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

"""
Change MEDIA_ROOT and MEDIA_URL according your Address.Address will be different for 
MAC/Windows/LINUX Servers. ( Where the Static Folder is Present)

This address are very import if you want to fetch your CSS,Images,Js,Jquery ...etc Everything 
Static is present in this folder.

Always use (/) instead of (\).

"""


STATIC_URL = '/static/'

MEDIA_ROOT = 'C:/Users/acer/Dwonloads/Django-Project-master/mysite/static/'

MEDIA_URL =   'C:/Users/acer/Dwonloads/Django-Project-master/mysite/static/'

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
)
