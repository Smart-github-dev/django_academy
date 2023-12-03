from django.http import JsonResponse
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError

# Create your views here.

def info(request):
    info = {
        'ENVIRONMENT': getattr(settings, 'ENVIRONMENT', None),
        'RELEASE': getattr(settings, 'RELEASE', None),
        'INSTANCE': getattr(settings, 'INSTANCE', None),
        'TIME_ZONE': getattr(settings, 'TIME_ZONE', None),
        'PAYPAL_TEST': getattr(settings, 'PAYPAL_TEST', None),
        'IS-DATABASE-UP': is_db_up(),
    }
    return JsonResponse(info)


def is_db_up():
    database_connection = connections['default']
    try:
        c = database_connection.cursor()
    except OperationalError:
        return False
    else:
        return True
