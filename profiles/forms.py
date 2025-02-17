from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import ProfileImage, UserProfile


class UserProfileCreationForm(UserCreationForm):
    """Form for creating a new user profile."""

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
    """Form for updating an existing user profile."""

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
            'interests': forms.Select(attrs={'placeholder': 'Interests'}),
            'font_family': forms.Select(attrs={'id': 'font-family-selector'}),
        }

    def __init__(self, *args, **kwargs):
        """Initialize the form and remove the password field."""
        super().__init__(*args, **kwargs)
        self.fields.pop('password')


class ProfileImageForm(forms.ModelForm):
    """Form for uploading a profile image."""

    class Meta:
        model = ProfileImage
        fields = ['image']
