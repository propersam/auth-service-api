from auth_service.settings.common import *

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', '(k)!m@k7aadsj27o@)vqb1s!93x$fksq7+m!6_r@1x%7%4l*bq')

# Allowed hosts (list of comma-separated host names, or asterisk to match all hosts), only needed if DEBUG is false
ALLOWED_HOSTS = ['testserver', '*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'DEFAULT-CHARACTER-SET': 'utf8',
        'NAME': 'sureeduauth',
        'USER': 'sureedu',
        'PASSWORD': 'sureedu',
        'HOST': 'db', # OR any host for the database
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    # },
}


BUGSNAG = {
    'api_key': '99ba4860115224b51cb380ec771e2450',
    'project_root': '/code/src'
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
