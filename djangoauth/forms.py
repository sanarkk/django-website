from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("First name"), widget=forms.TextInput(attrs={
            "class": "",
            "type": "",
            "placeholder": "First name",
        })
    )
    last_name = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("Last name"), widget=forms.TextInput(attrs={
            "class": "",
            "type": "",
            "placeholder": "Last name",
        })
    )
    email = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("Email"), widget=forms.TextInput(attrs={
            "class": "",
            "type": "",
            "placeholder": "Email",
        })
    )
    phone_number = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("Phone number"), widget=forms.TextInput(attrs={
            "class": "",
            "type": "",
            "placeholder": "Phone number",
        })
    )
    password1 = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("Password"), widget=forms.TextInput(attrs={
            "class": "",
            "type": "",
            "placeholder": "Password",
        })
    )
    password2 = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("Password"), widget=forms.TextInput(attrs={
            "class": "",
            "type": "",
            "placeholder": "Password",
        })
    )

    def save(self, request):
        user = super().save(request)
        p, _ = UserProfile.objects.get_or_create(user=user)
        return user
