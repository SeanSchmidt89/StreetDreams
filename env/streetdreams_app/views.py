from django.shortcuts import render
from django.views.generic import CreateView, DetailView,  DeleteView, ListView, UpdateView
from .models import *

# Create your views here.


class Index(ListView):
    model = Posts
    fields = '__all__'
    context_object_name = 'posts'
    template_name = 'streetdreams/index.html'

class Update(UpdateView):
    model = Posts
    fields = '__all__'
    context_object_name = 'post'
    template_name = 'streetdreams/update.html'