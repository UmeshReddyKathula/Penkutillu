from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeapp),
    path('login', views.loginuser, name='login'),
    path('signup', views.signupuser, name='signup'),
    path('logout', views.logout, name='logout'),
    path('display',views.allproducts)
] 