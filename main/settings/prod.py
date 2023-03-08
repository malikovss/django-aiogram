from .base import *

STATIC_ROOT = BASE_DIR / 'cdn' / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'cdn' / 'media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}
