# Regitser inside installed apps
# Make urls.py file

from django.urls import path
from .views import *

urlpatterns = [
    path('xyz/', my_xyz_view,),
    path('hello/', hello),
    path('hello/hi/', hello_hi)
]