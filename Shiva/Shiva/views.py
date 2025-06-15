from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse('<H1>Hello WOrld.</H1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')