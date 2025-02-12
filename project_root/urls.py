"""URL configuration."""

from django.contrib import admin
from django.urls import include, path

from home.views import hello_world

urlpatterns = [
    path('', hello_world),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
