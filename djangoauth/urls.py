from django.urls import path, re_path
from .views import CustomSignupView, CustomLoginView
from allauth.account import views


urlpatterns = [
    path("", CustomLoginView.as_view(), name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("signup/", CustomSignupView.as_view(), name="account_signup"),
    path(
        "password/change/",
        views.password_change,
        name="account_change_password",
    ),
    # E-mail
    path("email/", views.email, name="account_email"),
    path(
        "confirm-email/",
        views.email_verification_sent,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        views.confirm_email,
        name="account_confirm_email",
    ),
]
