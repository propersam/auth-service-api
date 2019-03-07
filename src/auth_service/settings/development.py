from auth_service.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(k)!m@k7aadsj27o@)vqb1s!93x$fksq7+m!6_r@1x%7%4l*bq'

# Allowed hosts (list of comma-separated host names, or asterisk to match all hosts), only needed if DEBUG is false
ALLOWED_HOSTS = ['testserver', '*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
	    'NAME': 'sureeduauth',
	    'USER': 'sureedu',
	    'PASSWORD': 'sureedu',
	    'HOST': 'localhost',
	    'PORT': '3306',
	    'DEFAULT-CHARACTER-SET': 'utf8',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    # },
}