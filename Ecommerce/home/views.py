from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login,logout
from .models import Product

# Create your views here.

def homeapp(request):
    return render(request,'home.html')

def loginuser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def signupuser(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        context['name'] = 'Penkutillu-Website Signup'

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username Taken')
            elif User.objects.filter(email=email).exists():
                print('Email Taken')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('Password Not Matching')
        return redirect('/')
        
    
    else:
        return render(request, 'signup.html',context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def allproducts(request):
    context={}
    data = Product.objects.all()
    context['products'] = data

    return render(request,'productwise.html',context)