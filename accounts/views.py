from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html',{})

def about(request):
    return render(request, 'accounts/about.html',{})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    