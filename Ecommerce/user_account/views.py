from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginuser(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request, username = uname, password = pwd)

        if user is not None:
            return HttpResponse(' he is valid user ')
    return render(request, 'dummy.html')