from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("First name")
    )
    last_name = forms.CharField(
        max_length=40, required=True, label=gettext_lazy("Last name")
    )
    phone_number = forms.CharField(
        max_length=40, required=False, label=gettext_lazy("Phone number")
    )

    def save(self, request):
        user = super().save(request)
        p, _ = UserProfile.objects.get_or_create(user=user)
        return user
