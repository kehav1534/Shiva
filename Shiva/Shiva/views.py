from django.http import HttpResponse
from django.shortcuts import render


def hompage(request):
    #return HttpResponse('<H1>Hello WOrld.</H1>')
    return render(request, 'home.html')

def about(request):
    return HttpResponse("My about page.")