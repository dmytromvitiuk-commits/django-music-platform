import os
import sys


app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if app_path not in sys.path:
    sys.path.append(app_path)

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()


app = application