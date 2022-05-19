from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
    path('post_details/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('create_post', CreatePost.as_view(), name='create_post')
]