from django.urls import path
from . import views

app_name='autoApp'

urlpatterns = [
    # path('demo',views.demo,name='demo'),
    path('',views.home,name='home_page'),
    path('about/',views.about,name='about_page'),
    path('vehicle/<int:vehicle_id/',views.detail,name="detail_page"),
]