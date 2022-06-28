from django.shortcuts import render

# Create your views here.

# Landing Page
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")