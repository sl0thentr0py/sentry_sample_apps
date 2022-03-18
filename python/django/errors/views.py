from django.http import HttpResponse
from .tasks import foobar_task

# Create your views here.
def bork(request):
    raise Exception("Test neel django exception")


def transaction(request, num):
    return HttpResponse(f"num {num}")


def rq_task(request):
    foobar_task.delay()
    return HttpResponse("Task run successful")
