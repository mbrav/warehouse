from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ijcmyjm9gl5cckfjxk2c4)3*zzipvxrr(npov*e5=b_ig)_vpy'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# Django Debug toolbar
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS.extend(('debug_toolbar',))
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
