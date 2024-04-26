from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def details(request):
    return render(request, 'details.html')


def contact(request):
    return HttpResponse("Contact: +919512345678")


def thanks(request):
    return HttpResponse("THANKS FOR VISITING!!")
