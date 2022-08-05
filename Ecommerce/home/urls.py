from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeapp),
    path('login', views.loginapp, name='login'),
]