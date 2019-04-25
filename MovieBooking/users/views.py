from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    # def get(self, request, *args,**kwargs):
    #     import ipdb;ipdb.set_trace()
        # return super()
# class SignIn(View):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'users/registration/login.html'

# Create your views here.
