from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
    return HttpResponse("<h1>Demo test</h1>")


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
