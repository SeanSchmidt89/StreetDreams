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
    vin = ''
    if 'car' in request.POST:
        vin = request.POST['car']
        api_key = 'ZrQEPSkKc2VhbnNjaG1pZHQ4OUB5YWhvby5jb20='
        url = 'https://auto.dev/api/vin/'+vin+'?apikey='+api_key 
        api_data = requests.get(url)
        json_data = api_data.json()
        print(json_data)
        make = json_data['make']['name']
        model = json_data['model']['name']
        context = {
            'make': make,
            'model': model,
        }
    else:
        context = {}
    
    
    

    return render(request, 'streetdreams_app/api.html', context)




    """    {
        'make': {
            'id': 200003381,
            'name': 'Toyota',
            'niceName': 'toyota'
            }, 
        'model': {
            'id': 'Toyota_Supra',
            'name': 'Supra',
            'niceName': 'supra'
            },
        'engine': {
            'id': '200503534',
            'name': 'Engine',
            'equipmentType': 'ENGINE',
            'availability': 'STANDARD',
            'cylinder': 6,
            'size': 3,
            'configuration': 'inline',
            'fuelType': 'regular unleaded',
            'horsepower': 320,
            'torque': 315,
            'type': 'gas',
            'code': '6ITTG3.0',
            'compressorType':
            'twin turbocharger',
            'rpm': {'horsepower': 5600, 'torque': 4000}
            },
        'transmission': {
            'id': '200503532', 
            'name': '6M', 
            'equipmentType': 'TRANSMISSION', 
            'availability': 'STANDARD', 
            'transmissionType': 'MANUAL', 
            'numberOfSpeeds': '6'}, 
        'drivenWheels': 'rear wheel drive', 
        'numOfDoors': '2', 
        'options': [], 
        'colors': [], 
        'price': {
            'usedTmvRetail': 30742, 
            'usedPrivateParty': 22286, 
            'usedTradeIn': 17212, 
            'estimateTmv': False
            }, 
        'categories': {
            'primaryBodyType': 'Car', 
            'market': 'Performance', 
            'epaClass': 'MINI_COMPACT_CARS', 
            'vehicleSize': 'Compact', 
            'vehicleType': 'Car', 
            'vehicleStyle': 'Coupe'}, 
        'squishVin': 'JT2JA82JP0', 
        'years':[
                {'id': 464, 
                'year': 1993, 
                'styles': [
                    {'id': 8890, 
                    'name': 'Turbo 2dr Coupe', 
                    'submodel': {
                        'body': 'Coupe', 
                        'modelName': 'Supra Coupe', 
                        'niceName': 'coupe'}, 
                        'trim': 'Base'
                    }
                        ]
                }
                    ], 
            'matchingType': 'SQUISHVIN', 
            'mpg': {'highway': '22', 'city': '15'}}
[22/May/2022 23:46:37] "POS"""