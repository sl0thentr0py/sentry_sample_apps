from django.http import HttpResponse
from .tasks import foobar_task
from sentry_sdk.hub import Hub

# Create your views here.
def bork(request):
    raise Exception("Test neel django exception")


def transaction(request, num):
    transaction = Hub.current.scope.transaction
    if transaction:
        transaction.set_measurement("neel.custom.metric", 123, unit="second")
    return HttpResponse(f"num {num}")


def rq_task(request):
    foobar_task.delay()
    return HttpResponse("Task run successful")
