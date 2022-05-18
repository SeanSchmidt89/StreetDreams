from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
]