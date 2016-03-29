from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def indexCaesarApp(request):
    return HttpResponse("Hello World, this is the CaesarApp index.")
