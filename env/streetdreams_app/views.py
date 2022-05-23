from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView,  DeleteView, ListView, UpdateView, FormView
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
import requests


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


class DeletePost(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('index')
    template_name = 'streetdreams_app/delete.html'


class UserLogin(LoginView):
    template_name = 'streetdreams_app/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')

class Register(FormView):
    template_name = 'streetdreams_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user) 
        return super(Register, self).form_valid(form)


def Api(request):
    if 'car' in request.POST:
        vin = request.POST['car']
        api_key = 'ZrQEPSkKc2VhbnNjaG1pZHQ4OUB5YWhvby5jb20='
        url = 'https://auto.dev/api/vin/'+vin+'?apikey='+api_key 
        api_data = requests.get(url)
        json_data = api_data.json()
        make = json_data['make']['name']
        model = json_data['model']['name']
        engine = json_data['engine']['configuration']
        cylinder = json_data['engine']['cylinder']
        compressortype = json_data['engine']['compressorType']
        year = json_data['years'][0]['year']
        type = json_data['categories']['vehicleStyle']
        horsepower = json_data['engine']['horsepower']
        highway = json_data['mpg']['highway']
        city = json_data['mpg']['city']
        
        context = {
            'make': make,
            'model': model,
            'engine': engine,
            'cylinder': cylinder,
            'compressortype': compressortype,
            'year': year,
            'type': type,
            'horsepower': horsepower,
            'highway': highway,
            'city': city,
        }
    else:
        context = {}

    return render(request, 'streetdreams_app/vininfo.html', context)