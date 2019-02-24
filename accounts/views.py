from django.shortcuts import render
from django.views import generic
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
# from .models import User
# from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'home.html')


def resetdone(request):
    return redirect('login')


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
