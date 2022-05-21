from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
    path('post_details/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
]