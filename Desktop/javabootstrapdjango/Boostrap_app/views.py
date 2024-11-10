

from django.shortcuts import render
from django.urls import path


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def therapist(request):
    return render(request,'therapist.html')