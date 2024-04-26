from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle


# Create your views here.


def home(request):
    vehicle = Vehicle.objects.all()
    context = {
        'vehicle_list': vehicle
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def detail(request, vehicle_id):
    vehicle=Vehicle.objects.get(id=vehicle_id)
    return render(request,"detail.html",{'vehicle':vehicle})
