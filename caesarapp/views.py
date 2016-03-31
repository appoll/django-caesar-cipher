from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .forms import UserInputForm


# Create your views here.

def index(request):
    return render(request, 'caesarapp/index.html', {})


def encrypt(request):
    return render(request, 'caesarapp/encrypt.html', {})


def about(request):
    return HttpResponse("Hello Universe")
