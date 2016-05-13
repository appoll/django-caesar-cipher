from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone

from caesarapp.CaesarCipher import CaesarCipher
from .models import UserInput
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
            return HttpResponseRedirect(reverse('encrypted', args=(userInput.id, )))
    else:
        form = UserInputForm()
    return render(request, 'caesarapp/encrypt.html', {'form': form})

def encrypted(request, userInput_id):
    userInput = get_object_or_404(UserInput, pk=userInput_id)
    caesarCipher = CaesarCipher(userInput.encryption_key)
    encryptedText = caesarCipher.encrypt(userInput.plain_text)
    return render(request, 'caesarapp/encrypted.html', {'userInput': userInput, 'encrypted': encryptedText})

def about(request):
    return HttpResponse("Hello Universe")

def history(request):
    latest_userInput_list = UserInput.objects.order_by('pub_date')
    template = loader.get_template('caesarapp/history.html')
    context = {
        'latest_userInput_list': latest_userInput_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'caesarapp/history.html', context)