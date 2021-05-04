from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.conf import settings
import os 

BASE_DIR = settings.BASE_DIR

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('loginUser')
        form = CreateUserForm()
        return render(request, os.path.join(BASE_DIR, 'templates/register.html'), {'form': form})

def loginUser(request):
    logout(request)
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, os.path.join(BASE_DIR, 'templates/login.html'), context)

def logoutUser(request):
    logout(request)
    return redirect('homepage')

def homepage(request):
    return HttpResponse("home page")
