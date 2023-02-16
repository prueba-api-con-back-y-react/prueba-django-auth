from django.shortcuts import render

from django.http import HttpResponse

def authPageView(request):
    return HttpResponse("Hello, World from Auth!!")
