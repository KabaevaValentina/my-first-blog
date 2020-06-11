from django.urls import path
from django.http import HttpResponse
from .views import ReviewListView, ReviewDetailView, ReviewCreate

def testView(request):
    return HttpResponse('<div align="center"><h1 style="color:blue">Это тестовая страница!</h1></div>')

urlpatterns=[
    path('', ReviewListView.as_view(), name='rev_list'),
    path('detail/<int:pk>', ReviewDetailView.as_view(), name='rev_detail'),
    path('create/', ReviewCreate.as_view(), name='rev_create'),
]