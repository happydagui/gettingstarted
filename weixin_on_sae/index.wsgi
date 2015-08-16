'''def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    import django
    msg = '.'.join([str(el) for el in django.VERSION])
    #return ['Hello, SAE!']
    return [msg]
'''

from django.conf import settings
import os
BASE_DIR = os.path.dirname(__name__)
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecret',
    ROOT_URLCONF='main',
    TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),),
    LOGGING={
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        },
    }
)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()