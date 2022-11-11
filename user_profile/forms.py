from django import forms
from djangoauth.models import UserProfile
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ["avatar", "phone_number"]

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

    #def save(self, request):
    #    user = super().save(request)
    #    first_name = self.cleaned_data["first_name"]
    #    last_name = self.cleaned_data["last_name"]
    #    p, _ = User.objects.get_or_create(
    #        user=user, first_name=first_name, last_name=last_name
    #    )
    #    return user

