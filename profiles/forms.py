from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import ProfileImage, UserProfile


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'profile_picture',
            'gender',
            'sexual_orientation',
            'age',
            'about',
            'interests',
            'theme',
            'font_family',
        )


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'profile_picture',
            'gender',
            'sexual_orientation',
            'age',
            'about',
            'interests',
            'theme',
            'font_family',
        )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'about': forms.Textarea(attrs={'placeholder': 'About'}),
            'interests': forms.Textarea(attrs={'placeholder': 'Interests'}),
            'font_family': forms.Select(attrs={'id': 'font-family-selector'}),
        }


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ['image']
