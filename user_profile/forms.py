from django import forms
from djangoauth.models import UserProfile
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ["avatar", "phone_number"]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self):
        profile = super().save(commit=True)
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        self.user.first_name = first_name
        self.user.last_name = last_name
        self.user.save()
        return profile

