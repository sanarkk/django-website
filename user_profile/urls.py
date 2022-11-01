from django.urls import path, re_path
from .views import ProfileView
from allauth.account import views


urlpatterns = [
    path("", ProfileView.as_view(), name="user_profile"),
]