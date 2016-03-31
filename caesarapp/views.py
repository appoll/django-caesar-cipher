from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .forms import UserInputForm


# Create your views here.

def index(request):
    return render(request, 'caesarapp/index.html', {})


def encrypt(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if (form.is_valid()):
            userInput = form.save(commit=False)
            userInput.pub_date = timezone.now()
            userInput.save()
    else:
        form = UserInputForm()
    return render(request, 'caesarapp/encrypt.html', {'form': form})


def about(request):
    return HttpResponse("Hello Universe")
