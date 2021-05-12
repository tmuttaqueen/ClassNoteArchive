from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.urls import reverse

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
        return render(request, 'users/register.html', {'form': form})

def loginUser(request):
    print ('starts....')
    return redirect('posts:homepage')
    if request.user.is_authenticated:
        return redirect('posts:homepage')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                print ('here.....')
                return redirect('posts:homepage')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('posts:homepage')