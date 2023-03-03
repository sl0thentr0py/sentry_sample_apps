import threading
from django.http import HttpResponse
from sentry_sdk import configure_scope

from .tasks import rq_task as rqt, celery_task as ct

# Create your views here.
def bork(request):
    raise Exception("Test neel django exception")

def scope1(request):
    with configure_scope() as scope:
        scope.set_tag("scope1", "foo")
        scope.set_tag("thread_id", threading.current_thread().ident)

    raise Exception("scope1 exc")

def scope2(request):
    with configure_scope() as scope:
        scope.set_tag("scope2", "bar")
        scope.set_tag("thread_id", threading.current_thread().ident)

    raise Exception("scope2 exc")

def transaction(request, num):
    return HttpResponse(f"num {num}")


def rq_task(request):
    rqt.delay()
    return HttpResponse("RQ Task run successful")


def celery_task(request):
    ct.delay()
    return HttpResponse("Celery Task run successful")
