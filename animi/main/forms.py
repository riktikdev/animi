from django import forms

from .models import Profile


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)


class ProfileBannerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_banner',)
