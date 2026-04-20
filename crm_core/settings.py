from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-23!)d=t959i-%_7rijcrjf)bv!(jb@vbm0@3a01!t+ka5rb%av'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm',
    'pwa',
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

ROOT_URLCONF = 'crm_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # MUITO IMPORTANTE
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crm_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True
DATE_INPUT_FORMATS = ['%d/%m/%Y', '%Y-%m-%d']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = '/static/'

# Esta pasta 'static' é a que aparece na sua foto da estrutura do projeto
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Esta pasta 'deploy_files' NÃO deve existir ainda. 
# O Django vai criar ela sozinho depois.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

JAZZMIN_SETTINGS = {
    "site_title": "CodeFlow CRM",
    "site_header": "CodeFlow CRM",
    "site_brand": "CodeFlow CRM",
    "welcome_sign": "Bem Vindo ao CodeFlow CRM",
    "copyright": "Zapflow - Codeflow",
    "search_model": ["crm.Cliente", "crm.Plano"],
    "show_ui_builder": False,
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "lumen",
}


# Caminho para onde os arquivos do PWA serão gerados
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

PWA_APP_NAME = 'CRM CodeFlow'
PWA_APP_DESCRIPTION = "Esse projeto é feito para gerenciar o clientes"
PWA_APP_THEME_COLOR = '#000000' # Cor da barra de tarefas/status
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone' # Faz abrir em janela própria, sem barra de navegador
PWA_APP_SCOPE = '/admin/'
PWA_APP_START_URL = '/admin/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_STATUS_BAR_COLOR = 'default'

# Ícones: Garanta que esse arquivo exista em static/images/
PWA_APP_ICONS = [
    {
        'src': '/static/IMG/icon-512.png',
        'sizes': '512x512'
    }
]

PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/IMG/icon-512.png',
        'sizes': '512x512'
    }
]