from django.urls import path
from .views import Home, CustomSignupView
from allauth.account import views as auth_view

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/', auth_view.login, name="account_login"),
    path('logout/', auth_view.logout, name="account_logout"),
    path('signup/', CustomSignupView.as_view(), name="account_signup"),
]