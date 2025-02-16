from django.urls import path

from . import views

urlpatterns = [
    path('', views.match_profiles, name='match_profiles'),
    path('auto-match/', views.auto_match_profiles, name='auto_match_profiles'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
]
