from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
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
            'profile_image',
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
        }
