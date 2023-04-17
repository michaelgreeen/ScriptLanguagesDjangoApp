from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as django_views
from .forms import UserLoginForm
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register", views.register_request, name="register"),
    path("created-sets/",views.created_sets_request,name="created-sets"),
    path("add-set/",views.add_set_request,name="add-set"),
    path("details/<int:pc_id>",views.details_request,name="details"),
    path('login/',django_views.LoginView.as_view(template_name="registration/login.html",authentication_form=UserLoginForm),name='login'),
    path('add_comment/<int:pc_id>',views.comment_add_request,name='add-comment'),
    path('delete-comment/<int:comment_id>/',views.comment_delete_request,name='delete-comment'),
    path('delete-pc-set/<int:pc_id>/',views.pc_set_delete_request,name='delete-pc-set'),
    path('edit-pc-set-view/<int:pc_id>/',views.pc_set_edit_view,name='edit-pc-set-view')
]