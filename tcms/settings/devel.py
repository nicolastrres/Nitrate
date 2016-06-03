# Django settings for devel env.
import os

from common import *

# Debug settings
from tcms.settings.common import TCMS_ROOT_PATH

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nitrate',
        'USER': 'nitrate',
    }
}

# django-debug-toolbar settings
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'south',
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# For local development
ENABLE_ASYNC_EMAIL = False

FIXTURE_DIRS = os.path.join(TCMS_ROOT_PATH, 'fixtures')
