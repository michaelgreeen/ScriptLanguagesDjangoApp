from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as django_views
from .models import UserLoginForm
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register", views.register_request, name="register"),
    path('login/',django_views.LoginView.as_view(template_name="registration/login.html",authentication_form=UserLoginForm),name='login')
    
]