import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_exhaust.settings')

app = Celery('data_exhaust')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
