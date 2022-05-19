from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView,  DeleteView, ListView, UpdateView
from .models import *
from .forms import *


# Create your views here.

class Index(ListView):
    model = Post
    fields = '__all__'
    context_object_name = 'posts'
    template_name = 'streetdreams_app/index.html'


class PostDetails(DetailView):
    model = Post
    fields = '__all__'
    context_object_name = 'post'
    template_name = 'streetdreams_app/post_details.html'


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'streetdreams_app/update.html'
    success_url = reverse_lazy('index')


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'streetdreams_app/create_post.html'
    success_url = reverse_lazy('index')