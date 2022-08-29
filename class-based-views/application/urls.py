from django.urls import path

from .views import HomeView

path('', HomeView.as_view(), name="home")  # class ise as_view gerekli