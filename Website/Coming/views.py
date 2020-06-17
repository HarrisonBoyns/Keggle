from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def coming(request):
    return render(request, "index.html")

def index(request):
    return HttpResponse("<h1>MyClub Event Calendar</h1>")