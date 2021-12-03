from django.shortcuts import render

# Create your views here.
def bork(request):
    raise Exception("Test neel django exception")
