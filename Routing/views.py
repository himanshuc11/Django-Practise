from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_xyz_view(requset):
    print(requset)
    return HttpResponse('This is my xyz view')

def hello(request):
    print('Hello was called')
    return HttpResponse('This is my hello view')

def hello_hi(request):
    print('I am on helllo hi route')
    return HttpResponse('Hello hi route')