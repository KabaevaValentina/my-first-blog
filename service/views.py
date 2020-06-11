from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Doctor, Service
from django.views import generic

# Create your views here.
class ServicesView(View):
    """Список услуг"""
    def get(self, request):
       services = Service.objects.all()
       return render(request, "main/service_list.html", {"service_list": services})


