import random
import string

from sentry_sdk import start_span
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Thing


# Create your views here.
def bork(request):
    password = "test"
    foo = 42
    custom_var = "bar"

    raise Exception("Test neel django exception")

def transaction(request, num):
    with start_span(op="neel span") as span:
        span.set_data("password", "test")
        span.set_data("bar", "cow")
        span.set_data("foo", 42)

        identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        for i in range(min(num, 50)):
            Thing(stuff=f"{identifier}_{i}", date=timezone.now()).save()

    return HttpResponse(f"num {num}")
