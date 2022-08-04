from django.shortcuts import render, HttpResponse

# Create your views here.

def loginuser(request):
    return render(request, 'login.html')