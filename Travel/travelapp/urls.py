from os import path
from django.urls import path
from travelapp import views

urlpatterns = [
    path('', views.homefun,name='homefun'),
]