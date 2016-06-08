from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return HttpResponse("Welcome to this page!")

def hello_view(request):
    return HttpResponse("Hello There!")

def balloon_view(request):
    return HttpResponse("99 Red Balllloooooooons!")

def extra_view(request):
    return HttpResponse("And one for good measure...")