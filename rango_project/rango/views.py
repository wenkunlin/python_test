from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {"boldmessage" : "candy !"}
    return render(request, 'index.html', context=context)
