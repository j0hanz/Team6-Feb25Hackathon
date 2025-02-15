from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
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
        ('default', 'Default'),
        ('serif', 'Serif'),
        ('sans-serif', 'Sans-serif'),
        ('dyslexie', 'Dyslexie'),
    ]

    profile_picture = CloudinaryField(
        'image',
        default='nobody_nrbk5n',
        blank=True,
        null=True,
        help_text='Upload a profile picture',
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    sexual_orientation = models.CharField(
        max_length=2, choices=SEXUAL_ORIENTATION_CHOICES, blank=True
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    theme = models.CharField(
        max_length=5, choices=THEME_CHOICES, default='light'
    )
    font_family = models.CharField(
        max_length=10, choices=FONT_FAMILY_CHOICES, default='default'
    )

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self) -> str:
        return self.username


@receiver(post_save, sender=UserProfile)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        pass
