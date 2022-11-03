from django import forms
from djangoauth.models import UserProfile
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone_number']
