from django.shortcuts import render
from django.views import generic
from .forms import ReviewForm
from .models import Review


class ReviewListView(generic.ListView):
    queryset = Review.objects.all()
    template_name = 'main/reviewlist.html'
    context_object_name = 'rev'

class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'main/reviewdetail.html'
    context_object_name = 'rev'

class ReviewCreate(generic.CreateView):
    form_class = ReviewForm
    template_name = 'main/reviewcreate.html'

# Create your views here.
