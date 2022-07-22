from django.http import HttpResponse
from .tasks import rq_task as rqt, celery_task as ct
from sentry_sdk.hub import Hub

# Create your views here.
def bork(request):
    raise Exception("Test neel django exception")


def transaction(request, num):
    return HttpResponse(f"num {num}")


def rq_task(request):
    rqt.delay()
    return HttpResponse("RQ Task run successful")


def celery_task(request):
    ct.delay()
    return HttpResponse("Celery Task run successful")
