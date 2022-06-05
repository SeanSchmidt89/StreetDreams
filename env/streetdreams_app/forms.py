from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
        }


class UserSignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserSignUp, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('car', 'profile_pic', 'pic_1', 'pic_2', 'pic_3', 'bio', 'mods')

        widgets = {
            'car': forms.TextInput(attrs={'class': 'form-control'}),
            #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            #'pic_1': forms.TextInput(attrs={'class': 'form-control'}),
            #'pic_2': forms.TextInput(attrs={'class': 'form-control'}),
            #'pic_3': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'mods': forms.Textarea(attrs={'class': 'form-control'}),
        }
