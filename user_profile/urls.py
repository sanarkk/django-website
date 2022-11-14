from django.urls import path, re_path
from .views import ProfileView, UpdateProfile
from allauth.account import views


urlpatterns = [
    path("<pk>/", ProfileView.as_view(), name="user_profile"),
    path('update/<pk>/', UpdateProfile.as_view(), name="account_update"),
]