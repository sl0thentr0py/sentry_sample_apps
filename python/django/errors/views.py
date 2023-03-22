import time
import threading
from django.http import HttpResponse
from sentry_sdk import configure_scope, add_breadcrumb, start_span

from .tasks import rq_task as rqt, celery_task as ct

# Create your views here.
def bork(request):
    password = "test"
    foo = 42
    custom_var = "bar"

    add_breadcrumb(dict(data={"foo": 42, "password": "test"}))
    raise Exception("Test neel django exception")

def scope1(request):
    with configure_scope() as scope:
        scope.set_tag("scope1", "foo")
        scope.set_tag("thread_id", threading.current_thread().ident)

    time.sleep(0.5)
    raise Exception("scope1 exc")

def scope2(request):
    with configure_scope() as scope:
        scope.set_tag("scope2", "bar")
        scope.set_tag("thread_id", threading.current_thread().ident)

    time.sleep(0.5)
    raise Exception("scope2 exc")

def transaction(request, num):
    with start_span(op="neel span") as span:
        span.set_data("password", "test")
        span.set_data("bar", "cow")
        span.set_data("foo", 42)
        time.sleep(0.1)

    return HttpResponse(f"num {num}")


def rq_task(request):
    rqt.delay()
    return HttpResponse("RQ Task run successful")


def celery_task(request):
    ct.delay()
    return HttpResponse("Celery Task run successful")
