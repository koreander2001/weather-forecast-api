import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD' : os.environ['POSTGRES_PASSWORD'],
        'HOST' : 'postgres',
        'PORT' : int(os.environ['POSTGRES_PORT']),
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = '/opt/static' #ボリュームマウント先のパス

