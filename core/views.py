from django.shortcuts import render
from django.http import HttpResponseRedirect
import forms

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CustomUserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.CustomUserCreationForm()

    return render(request, 'name.html', {'form': form})

def signin(request):
    return render(request, 'signin.html')

def ticket_view(request):
    return render(request, 'ticket_view.html')

def ticket_create(request):
    return render(request, 'ticket_create.html')

