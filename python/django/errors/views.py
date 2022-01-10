from django.http import HttpResponse

# Create your views here.
def bork(request):
    raise Exception("Test neel django exception")


def transaction(request, num):
    return HttpResponse(f"num {num}")
