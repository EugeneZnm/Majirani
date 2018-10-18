
from django.shortcuts import render, redirect


# importing login as auth_login to prevent clashing with inbuilt view
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Profile, Neighbourhood, Business

# import forms
from .forms import SignUpForm, EditProfileForm

# Create your views here.


# Home view function
def Home(request):

    return render(request, 'home.html')


# SIGNUP VIEW FUNCTION
def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validation
        if form.is_valid():
            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


# edit profile view function
@login_required(login_url='/registration/login/')
def profile_edit(request):
    """
    view function to render profile

    """
    form = EditProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if form.is_valid():
            form.save()

            return redirect('profile')

    return render(request, 'Profile/profile_edit.html', {'form': form})


# profile view function
@login_required(login_url='/registration/login/')
def profile(request):
    """
    view function to render profile

    """
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    return render(request, 'Profile/profile.html', {'profile': profile})