DEBUG = True
ALLOWED_HOSTS = []
print 'Check develop settings'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testing',
        'USER': 'postgres',
        'PASSWORD': '123123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'commons.decorators': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}