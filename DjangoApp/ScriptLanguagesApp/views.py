# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, user)
            messages.success(request, "Udało Ci się zalogować! :)")
            return redirect("index")
        messages.error(request, "Niepowodzenie. Sprawdź wpisane dane.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Udało Ci się zarejestrować! :)")
            return redirect("index")
        messages.error(request, "Niepowodzenie. Sprawdź wpisane dane.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})
