from django.shortcuts import render,HttpResponse

# Create your views here.

def homeapp(request):
    return render(request,'home.html')

#def loginapp(request):
 #   return render(request, 'login.html')

#def login2(request):
 #   return render(request, 'login2.html')