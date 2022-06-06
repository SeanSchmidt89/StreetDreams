from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView,  DeleteView, ListView, UpdateView, FormView
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
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
    form_class = UserSignUp
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user) 
        return super(Register, self).form_valid(form)


def Api(request):
    if request.GET:
        context ={}

    elif 'car' in request.POST and request.POST['car'] == '':
        invalid = 'Please enter a VIN Number'

        context = {'invalid': invalid}
        
    elif 'car' in request.POST:
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


class EditProfile(UpdateView):
    form_class = UserChangeForm
    template_name = 'streetdreams_app/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class ProfilePage(DetailView):
    model = Profile
    template_name = 'streetdreams_app/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['user_profile'] = user_profile
        return context


class EditProfilePage(UpdateView):
    model = Profile
    template_name = 'streetdreams_app/edit_profile_page.html'
    fields = ['bio', 'car', 'mods','profile_pic', 'pic_1', 'pic_2', 'pic_3']
    success_url = reverse_lazy('index')


class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'streetdreams_app/create_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)