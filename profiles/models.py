from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    """Model representing a user profile."""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-binary'),
        ('O', 'Other'),
    ]

    SEXUAL_ORIENTATION_CHOICES = [
        ('H', 'Heterosexual'),
        ('G', 'Gay'),
        ('L', 'Lesbian'),
        ('B', 'Bisexual'),
        ('A', 'Asexual'),
        ('P', 'Pansexual'),
        ('Q', 'Queer'),
        ('O', 'Other'),
    ]

    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    FONT_FAMILY_CHOICES = [
        ('serif', 'Merriweather'),
        ('Roboto', 'Roboto'),
        ('Lexend', 'Lexend'),
    ]

    AGE_RANGE_CHOICES = [
        ('18-25', '18-25'),
        ('25-30', '25-30'),
        ('30-35', '30-35'),
        ('35-40', '35-40'),
        ('40-45', '40-45'),
        ('45-50', '45-50'),
        ('50+', '50+'),
    ]

    profile_picture = CloudinaryField(
        'image',
        default='nobody_nrbk5n',
        blank=True,
        null=True,
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    sexual_orientation = models.CharField(
        max_length=2, choices=SEXUAL_ORIENTATION_CHOICES, blank=True
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)
    interests = models.CharField(
        max_length=2, choices=GENDER_CHOICES, blank=True
    )
    theme = models.CharField(
        max_length=5, choices=THEME_CHOICES, default='light'
    )
    font_family = models.CharField(
        max_length=10, choices=FONT_FAMILY_CHOICES, default='Roboto'
    )

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self) -> str:
        """Return the username of the user profile."""
        return self.username


class ProfileImage(models.Model):
    """Model representing a profile image."""

    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='gallery_images'
    )
    image = CloudinaryField('image')

    def __str__(self):
        """Return a string representation of the profile image."""
        return f"{self.user.username}'s image"


@receiver(post_save, sender=UserProfile)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile."""
    if created:
        pass
