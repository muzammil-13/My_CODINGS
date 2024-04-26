from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.addition,name='addition'),
    path('sub/',views.subtraction,name='subtraction'),
    path('mul/',views.multiplication,name="multiplication"),
    path('div/',views.division,name='division'),
]