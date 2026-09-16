from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import User


# Create your views here.

# class UserCreateView(CreateView):
#     model = User
    # form_class = UserCreationForm
    # success = reverse_lazy("users:login")


