from django.shortcuts import render,HttpResponse

# Create your views here.

def homeapp(request):
    return HttpResponse('i am umesh reddy')