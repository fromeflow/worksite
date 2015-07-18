# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'worksite.ini'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['Settings']['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config['Settings']['DEBUG']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'worksite.urls'

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

WSGI_APPLICATION = 'worksite.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['DB']['name'],
        'USER': config['DB']['user'],
        'PASSWORD': config['DB']['password'],
        'HOST': config['DB']['host'],
        'PORT': config['DB']['port']
    }
}


# Internationalization

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Chisinau'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


# Templates settings

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)