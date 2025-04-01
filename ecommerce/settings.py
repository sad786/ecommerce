

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-=hc!k+3+s&n$8&0p-#t#bpv$bya+ahq7u5km9fx4)7uum8ycq('

import os
from pathlib import Path
from decouple import config
import boto3
boto3.set_stream_logger('')
#import environ

#import dj_database_url

#print(env('ENGINE'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-=hc!k+3+s&n$8&0p-#t#bpv$bya+ahq7u5km9fx4)7uum8ycq(')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG') == 'True'

ALLOWED_HOSTS = [ 'localhost','127.0.0.1','ecommerce-jn1h.onrender.com']

#ALLOWED_HOSTS = [os.getenv('RENDER_PUBLIC_DOMAIN', default='localhost')]



AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME =config('AWS_BUCKET_NAME')
AWS_S3_REGION_NAME="eu-north-1"
AWS_S3_CUSTOM_DOMAIN=f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS ={'CacheControl':'max-age=86400'}
AWS_DEFAULT_ACL= None

AWS_S3_SIGNATURE_VERSION = 's3v4'       # Force v4 signatures
AWS_S3_ADDRESSING_STYLE = 'virtual'      # Required for newer regions

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'store.apps.StoreConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'accounts.apps.AccountsConfig',
    
    # Third-party apps
    'crispy_forms',
    'crispy_bootstrap4',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',  # Make cart available in all templates
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'DATABASE_URL': config('DATABASE_URL'),
        
        'ENGINE': config('ENGINE'),

        'NAME': config('NAME'), 

        'USER': config('USER'), 

        'PASSWORD': config('PASSWORD'),

        'HOST': config('HOST'), 

        'PORT': config('PORT'),

        'OPTIONS': {
            'sslmode':'require',
        },
    },
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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = [
#    BASE_DIR / 'static',
    os.path.join(BASE_DIR,'static'),
]

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# here media files will be sotred
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media files
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

#MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Authentication
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Session settings for cart
CART_SESSION_ID = 'cart'

# PayPal settings
PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID', '')
PAYPAL_SECRET_KEY = os.environ.get('PAYPAL_SECRET_KEY', '')
PAYPAL_MODE = os.environ.get('PAYPAL_MODE', 'sandbox')  # 'sandbox' or 'live'

# Message tags for Bootstrap
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
