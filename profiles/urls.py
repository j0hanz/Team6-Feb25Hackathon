from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile_page, name='profile'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('profile-page/', views.profile_page_view, name='profile_page_view'),
]
