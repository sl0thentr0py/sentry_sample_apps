from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery
from celery.decorators import periodic_task

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sentry.settings')

app = Celery('sentry')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# @periodic_task(run_every=timedelta(seconds=5))
def secondly():
    print("wassup")
    debug_task.apply_async()

