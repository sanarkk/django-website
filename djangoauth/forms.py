from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator
from core.settings.base import LANGUAGES
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

    email = forms.EmailField()

    phone_number = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r"^\+?1?\d{9,15}$",
                message="Enter a Valid Phone Number",
            )
        ],
    )

    language = forms.ChoiceField(choices=LANGUAGES)

    def save(self, request):
        user = super().save(request)
        phone_number = self.cleaned_data["phone_number"]
        language = self.cleaned_data["language"]
        p, _ = UserProfile.objects.get_or_create(
            user=user, phone_number=phone_number, language=language
        )
        return user
