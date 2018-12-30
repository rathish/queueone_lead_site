from .base import *

DEBUG = False
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e590r!w0-5@mcsl+i7l81*@5l#s_h&5#jebd7&_dnu+0f!yb5-'

try:
    from .local import *
except ImportError:
    pass
