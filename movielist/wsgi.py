import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
project_home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Get the WSGI application
application = get_wsgi_application()