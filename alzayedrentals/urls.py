from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('service',views.service, name='service'),
    path('about',views.about,name='about'),
    path('equipments',views.equipment,name='equipment'),
    path('contact',views.contact,name='contactus')
]
