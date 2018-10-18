
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

# importing login as auth_login to prevent clashing with inbuilt view
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Profile, Neighbourhood, Business

# import forms
from .forms import SignUpForms

# Create your views here.
