from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('/creator', views.creator_view, name='creator')
]