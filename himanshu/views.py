from curses.ascii import HT
from dataclasses import field
import email
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import People, Todo

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django import forms
# Todo Form
class TodoForm(forms.Form):
    todo = forms.IntegerField(label="Todo")

# Model Forms
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    

# Create your views here.
def index(request):
    if request.method == "GET":
        unbound_form = TodoForm()
        return render(request, 'home.html', {"form": unbound_form})
    if request.method == "POST":
        bounded_form = TodoForm(request.POST)
        if bounded_form.is_valid():
            todo = bounded_form.cleaned_data['todo']
            new_todo = Todo(todo=todo)
            new_todo.save()
        else:
            print('ERRRRRRRROR')
            return HttpResponse("Errors" + str(bounded_form.errors))
        return render(request, "home.html", {"form": TodoForm()})
        


def contact(request):
    return render(request, 'contact.html')


def sign_in(request):
    if request.method == "GET":
        return render(request, 'sign_in.html')
    if request.method == "POST":
        print(request.POST['username'], request.POST['password'])
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return HttpResponse('You are successfully logged in')
        else:
            return HttpResponse('You are invalid user')

def sign_up(request):
    if request.method == "GET":
        return render(request, 'sign_up.html', {"form": RegisterForm()})

    if request.method == "POST":
        bounded_form = RegisterForm(request.POST)
        if bounded_form.is_valid():
            username = bounded_form.cleaned_data['username']
            password = bounded_form.cleaned_data['password']
            email = bounded_form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponse('Success')
        else:
            return HttpResponse(bounded_form.errors)




## Templates + HW({{operation}} results in {{result}})

# url 'url_name'
# block Empty space
# extend Inheritance