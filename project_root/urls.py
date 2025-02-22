"""URL configuration."""

from django.contrib import admin
from django.urls import include, path

from home.views import hello_world

urlpatterns = [
    path('', hello_world, name='home'),
    path('match/', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('profiles/', include('profiles.urls')),
]
