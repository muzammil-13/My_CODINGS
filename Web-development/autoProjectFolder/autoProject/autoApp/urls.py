from django.urls import path
from . import views

urlpatterns = [
    path('demo',views.demo,name='demo'),
    path('',views.home,name="home_page"),
    path('about/',views.about,name="about_page"),
]