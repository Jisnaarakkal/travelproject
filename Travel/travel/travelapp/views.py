from django.http import HttpResponse
from django.shortcuts import render
from .models import demoapp_place
from .models import people

# Create your views here.

def homefun(request):
    obj = demoapp_place.objects.all()
    pplobj=people.objects.all()
    return render(request,"index.html",{'result':obj,'pplres':pplobj})

# def homefun(request):
#     return render(request, "index.html")