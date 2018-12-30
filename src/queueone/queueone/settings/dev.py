from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e590r!w0-5@mcsl+i7l81*@5l#s_h&5#jebd7&_dnu+0f!yb5-'

ALLOWED_HOSTS =['queueone.co.in']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
