from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> I am here </h1>")

def custfunc(request):
    return HttpResponse("<p> There is nothing to show. Please select other options")
