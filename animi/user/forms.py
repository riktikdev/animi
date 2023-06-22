from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)


class ProfileBannerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_banner',)
