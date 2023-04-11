from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from DjangoApp.authentication.AuthenticationModule import AuthenticationModule
#from AuthenticationModule import *
from common.logging import LOGGER

def register(request):
    LOGGER.info('User trying to register')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            LOGGER.info(user)
            login(request)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    LOGGER.info('User trying to sign in')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            result = AuthenticationModule.authorize(form.get_user())
            if result:
                LOGGER.info('User successfully authenticated')
                return redirect('')
    else:
        form = AuthenticationForm()
    LOGGER.info('User could not have been authenticated')
    return render(request, 'login.html', {'form': form})
