from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile, Languages
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


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
        max_length=15,
        validators=[
            RegexValidator(
                r"^\+?1?\d{9,15}$",
                message="Enter a Valid Phone Number",
            )
        ],
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
