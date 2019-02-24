from django.shortcuts import render
from django.utils.formats import date_format
from django.views import generic
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile, Address, events
from datetime import datetime
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User

from .models import venue

# from django.http import HttpResponse
# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'home.html')


def profile(request):
    profile_set = Profile.objects.filter(user=request.user)
    for i in profile_set:
        profile = i
    address_set = Address.objects.filter(user=request.user)
    address=0
    for i in address_set:
        address = i
    event = events.objects.filter(user=request.user)
    eventcount = event.count()
    remainingeventcount = event.filter(date__gte=datetime.now()).count()
    context = {'profile': profile, 'address': address, 'eventcount': eventcount,'remainingeventcount':remainingeventcount}
    return render(request, 'userdetails.html', context)



def login(request):
    return render(request, 'registration/login.html')


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EventListView(LoginRequiredMixin,ListView):
    model = events
    template_name = ''
    context_object_name = 'events'
    def get_queryset(self):
        return events.objects.filter(user=self.request.user)


class AddressCreateView(LoginRequiredMixin,CreateView):
    model = Address
    template_name ='WebApp/Address_CreateView.html'
    success_url = '/profile/'
    fields =['addressline','street','area','city','state','pincode','country']
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class AddressUpdateView(LoginRequiredMixin,UpdateView):
    model = Address
    template_name ='WebApp/Address_CreateView.html'
    success_url = '/profile/'
    fields =['addressline','street','area','city','state','pincode','country']
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_object(self, queryset=None):
        return Address.objects.get(user=self.request.user)



class ProfileCreateView(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'WebApp/Profile_CreateView.html'
    success_url = '/profile/'
    fields =['image','contact','date_of_birth','gender']
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'WebApp/Profile_CreateView.html'
    success_url = '/profile/'
    fields =['image','contact','date_of_birth','gender']

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

'''id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    gender_choices = (('m', 'Male'),('f', 'Female'),('o','other'))
    gender = models.CharField(max_length=10, choices=gender_choices)'''