from django.http import request
from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    # return HttpResponse('this about me page!')
    return render(request, 'about.html')


def home(request):
    # return HttpResponse('this is home page!')
    return render(request, 'home.html')
