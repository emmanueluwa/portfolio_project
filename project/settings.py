"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import mimetypes
mimetypes.add_type("text/css", ".css", True)

WHITENOISE_MIMETYPES = {
    '.xsl': 'application/xml'
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=moczgv@gkoq-g-k(98%lrs!3t$*568f0bn!1-pniw%be51ki9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "portfolio_project.apps.PortfolioProjectConfig",
    'django_sass',
    'ckeditor',
    'crispy_forms',
    'ckeditor_uploader',

]

CRISPY_FORMS_PACK = 'bootstrap4'
CKEDITOR_UPLOAD_PATH = 'uploads/'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware' ,

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "portfolio_project/template/portfolio_project")],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "portfolio_project_db",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


###################  for development #################
#route for web browser
STATIC_URL = '/portfolio_project/static/'

#route for django
STATICFILES_DIRS = [
    os.path.join(BASE_DIR , 'portfolio_project/static/portfolio_project/' )
]

MEDIA_URL = '/media/'
######################################################

# VENV_PATH =os.path.dirname(BASE_DIR)
# STATIC_ROOT = os.path.join(VENV_PATH, 'portfolio_project/static/portfolio_project/static_root')

# MEDIA_URL = 'portfolio_project/static/portfolio_project/images/'


## AWS S3, Cloudfront
# STATIC_ROOT = [
#     BASE_DIR , 'cdn_test' 
# ]

# MEDIA_ROOT = [
#     BASE_DIR , 'cdn_test' 
# ]





EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "fulonline1@gmail.com"
EMAIL_HOST_PASSWORD = "dlphwewaaladnlif"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
 