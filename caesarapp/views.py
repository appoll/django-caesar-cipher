from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import UserInput
from .forms import UserInputForm
import pdb

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
            pdb.set_trace()
            return HttpResponseRedirect(reverse('encrypted', args=(userInput.id, )))
    else:
        form = UserInputForm()
    return render(request, 'caesarapp/encrypt.html', {'form': form})

def encrypted(request, userInput_id):
    pdb.set_trace()
    userInput = get_object_or_404(UserInput, pk=userInput_id)
    response = "You're looking at the encryption of your message \"%s\"."
    return HttpResponse(response % userInput.plain_text)


def about(request):
    return HttpResponse("Hello Universe")
