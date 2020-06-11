from django.contrib import admin
from .models import Category, Doctor, Service, Analysis



admin.site.register(Category)
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Analysis)

# Register your models here.
