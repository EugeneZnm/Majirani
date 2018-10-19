from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Neighbourhood, Business, Comment, Post

from django.contrib.auth.models import User


# signup form adding custom field
class SignUpForm(UserCreationForm):
    """
    user creation form for sigup, adding custom field to signup form

    """
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


# Form for editing profile
class EditProfileForm(forms.ModelForm):
    """
    form for editing profile
    """
    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'bio', 'email']


class NeighbourhoodForm(forms.ModelForm):
    """
    form to create neighbourhood by users
    """
    class Meta:
        model = Neighbourhood
        exclude =['admin', 'biz']
        fields =['image', 'name', 'location', 'police', 'Hospital']