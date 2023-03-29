from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from . import forms

# Create your views here.

def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def login(request):
    return render(request, 'login.html')

def ticket_view(request):
    return render(request, 'ticket_create.html')

def ticket_create(request):
    return render(request, 'ticket_create.html')

