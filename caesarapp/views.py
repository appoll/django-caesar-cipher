from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'caesarapp/index.html', {})

def about(request):
    return HttpResponse("Hello Universe")