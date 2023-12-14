import os
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1','www.stmarksstandardsecondaryschool.com','stmarksstandardsecondaryschool.com','web-production-90ba.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_logs',
    'Accounts',
    'Admission_form',
    'CBT',
    'Payment_portal',
    'Result_portal',
    'Teachers_Portal',
    'Blog',
    'Elibrary',
    'Home',
    "django_cleanup",
    "ckeditor"
]

DJANGO_ADMIN_LOGS_DELETABLE = True
DJANGO_ADMIN_LOGS_ENABLED = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
from django.contrib import messages
MESSAGE_TAGS = {
			messages.DEBUG: 'alert-secondary',
			messages.INFO: 'alert-info',
			messages.SUCCESS: 'alert-success',
			messages.WARNING: 'alert-warning',
			messages.ERROR: 'alert-danger',
}

ROOT_URLCONF = 'smsssite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'smsssite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


import dj_database_url
db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = 'Accounts:login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS= [os.path.join(BASE_DIR, "assets"),]

MEDIA_URL= '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')

# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
# AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS={'CacheControl':'max-age=86400'}
# AWS_S3_REGION_NAME = 'us-east-1'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE='smsssite.storages.MediaStore'
# AWS_LOCATION = 'static'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets"),]
# STATIC_URL='https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)


# EMAIL_BACKEND='sendgrid_backend.SendgridBackend'
# SENDGRID_API_KEY = config('SENDGRID_API_KEY', default='')
# SENDGRID_SANDBOX_MODE_IN_DEBUG=config('SENDGRID_SANDBOX_MODE_IN_DEBUG', default=False, cast=bool)

# PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY', default='')
# PAYSTACK_SECRET_KEY = config('PAYSTACK_SECRET_KEY', default='')

PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY')
PAYSTACK_SECRET_KEY = config('PAYSTACK_SECRET_KEY')


MAPBOXGL_ACCESSTOKEN=config('MAPBOXGL_ACCESSTOKEN', default='')

# if os.getcwd() == '/app':
# 	SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDING_PROTO','https')
# 	SECURE_SSL_REDIRECT=True


JAZZMIN_SETTINGS = {
    "site_logo": "images/St Marks Logo.png",
    "site_logo_classes": "img-circle",
    "login_logo": None,
    "copyright": "St Marks Standard Secondary School Omagba",
    "show_ui_builder":True,
    "custom_css": "css/admin.css",
}

CKEDITOR_CONFIGS = {
    'default': {
        'height': '300px',
        'width': '100%',
        # 'toolbar': [
        #     ['Format', 'Font', 'FontSize', 'TextColor', 'BGColor'],
        #     ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        #     ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
        #     ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
        #     ['Maximize'],
        #     ['Source', 'Undo', 'Redo']
        # ],
        # 'font_size': '12px',
        # 'colorButton_colors': '000000,ffffff'
    }
}