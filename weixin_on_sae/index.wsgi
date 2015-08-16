'''def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    import django
    msg = '.'.join([str(el) for el in django.VERSION])
    #return ['Hello, SAE!']
    return [msg]
'''

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecret',
    ROOT_URLCONF='main',
)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()