from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=40,
        required=True,
    )
    last_name = forms.CharField(
        max_length=40,
        required=True,
    )
    email = forms.CharField(
        max_length=40,
        required=True,
    )
    phone_number = forms.CharField(
        max_length=40,
        required=True,
    )
    password1 = forms.CharField(
        max_length=40,
        required=True,
    )
    password2 = forms.CharField(
        max_length=40,
        required=True,
    )

    def save(self, request):
        user = super().save(request)
        p, _ = UserProfile.objects.get_or_create(user=user)
        return user
