DEBUG = False
ALLOWED_HOSTS = ['*']
print 'Check poduction settings'

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