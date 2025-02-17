from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile_page, name='profile'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('profile-page/', views.profile_page_view, name='profile_page_view'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='account/password_change.html'
        ),
        name='password_change',
    ),
    path(
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='account/password_change_done.html'
        ),
        name='password_change_done',
    ),
]
